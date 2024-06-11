from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models.Utilisateur import Utilisateur
from models.Garage import Garage
from models.Police import Police
from models.Admin import Admin
from app import db

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/signup/<string:role>', methods=['POST'])
def signup(role='utilisateur'):
    data = request.get_json()

    required_fields = ['nom', 'prenom', 'email', 'adresse', 'telephone', 'motDePasse']
    missing_fields = [field for field in required_fields if field not in data or not data[field]]
    if missing_fields:
        return jsonify({"error": f"Les champs suivants sont manquants ou vides: {', '.join(missing_fields)}"}), 400

    if Utilisateur.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Un utilisateur avec cet email existe déjà."}), 400

    if role not in ['admin', 'garage', 'police', 'utilisateur']:
        return jsonify({"error": "Rôle non valide."}), 400

    # Définir le modèle à utiliser en fonction du rôle
    if role == 'admin':
        user = Admin(
            nom=data['nom'],
            prenom=data['prenom'],
            email=data['email'],
            adresse=data['adresse'],
            telephone=data['telephone'],
            type='admin'
        )
    elif role == 'garage':
        user = Garage(
            nom=data['nom'],
            prenom=data['prenom'],
            email=data['email'],
            adresse=data['adresse'],
            telephone=data['telephone'],
            nomGarage=data['nomGarage'],
            adresseGarage=data['adresseGarage'],
            type='garage'
        )
    elif role == 'police':
        user = Police(
            nom=data['nom'],
            prenom=data['prenom'],
            email=data['email'],
            adresse=data['adresse'],
            telephone=data['telephone'],
            nomDepartement=data['nomDepartement'],
            adresseDepartement=data['adresseDepartement'],
            type='police'
        )
    else:
        user = Utilisateur(
            nom=data['nom'],
            prenom=data['prenom'],
            email=data['email'],
            adresse=data['adresse'],
            telephone=data['telephone'],
            type='utilisateur'
        )

    user.motDePasse = generate_password_hash(data['motDePasse'])
    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity={'utilisateurId': user.utilisateurId, 'type': user.type})
    return jsonify({"message": f"{role.capitalize()} créé avec succès", "access_token": access_token}), 201

# Ajoutez ici d'autres routes d'authentification comme le login


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
