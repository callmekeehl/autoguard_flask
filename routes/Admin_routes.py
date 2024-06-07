# routes/admin_routes.py
from flask import Blueprint, request, jsonify
from models.Admin import Admin
from models.Utilisateur import Utilisateur
from app import db

admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route('/admins', methods=['POST'])
def create_admin():
    data = request.get_json()

    # Crée d'abord l'utilisateur de base
    new_user = Utilisateur(
        nom=data['nom'],
        prenom=data['prenom'],
        email=data['email'],
        adresse=data['adresse'],
        telephone=data['telephone'],
        type='admin'  # Indique que cet utilisateur est un admin
    )
    new_user.motDePasse = data['motDePasse']
    db.session.add(new_user)
    db.session.commit()

    # Ensuite, crée l'admin spécifique
    new_admin = Admin(
        utilisateurId=new_user.utilisateurId,
        champSpecifiqueAdmin=data.get('champSpecifiqueAdmin', '')  # Exemple de champ spécifique
    )
    db.session.add(new_admin)
    db.session.commit()

    return jsonify({"message": "Admin créé", "adminId": new_admin.adminId}), 201


@admin_bp.route('/admins', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    return jsonify([a.to_dict() for a in admins])


@admin_bp.route('/admins/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_admin(id):
    admin = Admin.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(admin.to_dict())

    if request.method == 'PUT':
        data = request.get_json()

        # Mettez à jour les champs de l'utilisateur de base
        utilisateur = Utilisateur.query.get(admin.utilisateurId)
        utilisateur.nom = data['nom']
        utilisateur.prenom = data['prenom']
        utilisateur.email = data['email']
        utilisateur.adresse = data['adresse']
        utilisateur.telephone = data['telephone']
        if 'motDePasse' in data:
            utilisateur.motDePasse = data['motDePasse']

        # Mettez à jour les champs spécifiques à l'admin
        admin.champSpecifiqueAdmin = data.get('champSpecifiqueAdmin', '')
        db.session.commit()

        return jsonify({"message": "Admin mis à jour"})

    if request.method == 'DELETE':
        # Supprimez d'abord l'entrée admin
        db.session.delete(admin)
        db.session.commit()

        # Ensuite, supprimez l'utilisateur de base
        utilisateur = Utilisateur.query.get(admin.utilisateurId)
        db.session.delete(utilisateur)
        db.session.commit()

        return jsonify({"message": "Admin supprimé"})
