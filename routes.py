# routes.py
from flask import Blueprint, request, jsonify
from models.Utilisateur import Utilisateur
from app import db

main = Blueprint('main', __name__)

@main.route('/utilisateurs', methods=['GET', 'POST'])
def handle_utilisateurs():
    if request.method == 'POST':
        data = request.get_json()
        new_user = Utilisateur(
            nom=data['nom'],
            prenom=data['prenom'],
            email=data['email'],
            adresse=data['adresse'],
            telephone=data['telephone'],
            motDePasse=data['motDePasse']
        )
        new_user.motDePasse = data['motDePasse']  # Utiliser le setter pour hacher le mot de passe
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Utilisateur créé"}), 201

    if request.method == 'GET':
        utilisateurs = Utilisateur.query.all()
        return jsonify([u.to_dict() for u in utilisateurs])

@main.route('/utilisateurs/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_utilisateur(id):
    utilisateur = Utilisateur.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(utilisateur.to_dict())

    if request.method == 'PUT':
        data = request.get_json()
        utilisateur.nom = data['nom']
        utilisateur.prenom = data['prenom']
        utilisateur.email = data['email']
        utilisateur.adresse = data['adresse']
        utilisateur.telephone = data['telephone']
        utilisateur.motDePasse = data['motDePasse']
        db.session.commit()
        return jsonify({"message": "Utilisateur mis à jour"})

    if request.method == 'DELETE':
        db.session.delete(utilisateur)
        db.session.commit()
        return jsonify({"message": "Utilisateur supprimé"})
