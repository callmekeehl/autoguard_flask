from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models.Utilisateur import Utilisateur
from app import db

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Les données sont manquantes"}), 400

    # Vérifiez que tous les champs requis sont présents
    required_fields = ['nom', 'prenom', 'email', 'adresse', 'telephone', 'motDePasse']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"Le champ {field} est manquant"}), 400

    # Vérifiez si l'utilisateur existe déjà
    if Utilisateur.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Un utilisateur avec cet email existe déjà"}), 400

    # Créez le nouvel utilisateur
    new_user = Utilisateur(
        nom=data['nom'],
        prenom=data['prenom'],
        email=data['email'],
        adresse=data['adresse'],
        telephone=data['telephone'],
        type='utilisateur'  # Type par défaut pour les nouveaux utilisateurs
    )
    new_user.motDePasse = generate_password_hash(data['motDePasse'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Utilisateur créé avec succès"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'email' not in data or 'motDePasse' not in data:
        return jsonify({"error": "Email et mot de passe requis"}), 400

    user = Utilisateur.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.motDePasse, data['motDePasse']):
        return jsonify({"error": "Email ou mot de passe incorrect"}), 401

    # Créez un token d'accès
    access_token = create_access_token(identity={'utilisateurId': user.utilisateurId, 'type': user.type})
    return jsonify({"access_token": access_token}), 200
