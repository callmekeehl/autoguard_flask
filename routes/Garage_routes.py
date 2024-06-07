# routes/garage_routes.py
from flask import Blueprint, request, jsonify
from models.Garage import Garage
from models.Utilisateur import Utilisateur
from app import db

garage_bp = Blueprint('garage_bp', __name__)


@garage_bp.route('/garages', methods=['GET', 'POST'])
def handle_garages():
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
        new_garage = Garage(
            utilisateurId=utilisateur.utilisateurId,
            nomGarage=data['nomGarage'],
            adresseGarage=data['adresseGarage']
        )
        db.session.add(new_garage)
        db.session.commit()
        return jsonify({"message": "Garage créé"}), 201

    if request.method == 'GET':
        garages = Garage.query.all()
        return jsonify([g.to_dict() for g in garages])


@garage_bp.route('/garages/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_garage(id):
    garage = Garage.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(garage.to_dict())

    if request.method == 'PUT':
        data = request.get_json()
        utilisateur = garage.utilisateur
        utilisateur.nom = data['nom']
        utilisateur.prenom = data['prenom']
        utilisateur.email = data['email']
        utilisateur.adresse = data['adresse']
        utilisateur.telephone = data['telephone']
        garage.nomGarage = data['nomGarage']
        garage.adresseGarage = data['adresseGarage']
        if 'motDePasse' in data:
            utilisateur.motDePasse = data['motDePasse']
        db.session.commit()
        return jsonify({"message": "Garage mis à jour"})

    if request.method == 'DELETE':
        db.session.delete(garage)
        db.session.commit()
        return jsonify({"message": "Garage supprimé"})
