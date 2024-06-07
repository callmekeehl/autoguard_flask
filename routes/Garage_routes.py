# routes/garage_routes.py
from flask import Blueprint, request, jsonify
from models.Garage import Garage
from app import db

garage_bp = Blueprint('garage_bp', __name__)

@garage_bp.route('/garages', methods=['GET', 'POST'])
def handle_garages():
    if request.method == 'POST':
        data = request.get_json()
        new_garage = Garage(
            nom=data['nom'],
            prenom=data['prenom'],
            email=data['email'],
            adresse=data['adresse'],
            telephone=data['telephone'],
            nomGarage=data['nomGarage'],
            adresseGarage=data['adresseGarage']
        )
        new_garage.motDePasse = data['motDePasse']  # Utilise le setter pour hacher le mot de passe
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
        garage.nom = data['nom']
        garage.prenom = data['prenom']
        garage.email = data['email']
        garage.adresse = data['adresse']
        garage.telephone = data['telephone']
        garage.nomGarage = data['nomGarage']
        garage.adresseGarage = data['adresseGarage']
        if 'motDePasse' in data:
            garage.motDePasse = data['motDePasse']  # Utilise le setter pour hacher le mot de passe
        db.session.commit()
        return jsonify({"message": "Garage mis à jour"})

    if request.method == 'DELETE':
        db.session.delete(garage)
        db.session.commit()
        return jsonify({"message": "Garage supprimé"})
