# routes/admin_routes.py
from flask import Blueprint, request, jsonify
from models.Admin import Admin
from models.Utilisateur import Utilisateur
from app import db

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admins', methods=['GET', 'POST'])
def handle_admins():
    if request.method == 'POST':
        data = request.get_json()
        utilisateur = Utilisateur(
            nom=data['nom'],
            prenom=data['prenom'],
            email=data['email'],
            adresse=data['adresse'],
            telephone=data['telephone']
        )
        utilisateur.motDePasse = data['motDePasse']
        db.session.add(utilisateur)
        db.session.flush()  # Flush pour obtenir l'ID utilisateur
        new_admin = Admin(utilisateurId=utilisateur.utilisateurId)
        db.session.add(new_admin)
        db.session.commit()
        return jsonify({"message": "Admin créé"}), 201

    if request.method == 'GET':
        admins = Admin.query.all()
        return jsonify([a.to_dict() for a in admins])

@admin_bp.route('/admins/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_admin(id):
    admin = Admin.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(admin.to_dict())

    if request.method == 'PUT':
        data = request.get_json()
        utilisateur = admin.utilisateur
        utilisateur.nom = data['nom']
        utilisateur.prenom = data['prenom']
        utilisateur.email = data['email']
        utilisateur.adresse = data['adresse']
        utilisateur.telephone = data['telephone']
        if 'motDePasse' in data:
            utilisateur.motDePasse = data['motDePasse']
        db.session.commit()
        return jsonify({"message": "Admin mis à jour"})

    if request.method == 'DELETE':
        db.session.delete(admin)
        db.session.commit()
        return jsonify({"message": "Admin supprimé"})
