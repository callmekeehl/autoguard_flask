# routes.py
from flask import Blueprint, request, jsonify
from models import Declaration, Notification, Rdv, Police, Garage
from models.Utilisateur import Utilisateur
from app import db

main = Blueprint('main', __name__)


@main.route('/garages', methods=['GET', 'POST'])
def handle_garages():
    if request.method == 'POST':
        data = request.get_json()
        new_garage = Garage(
            nomGarage=data['nomGarage'],
            adresseGarage=data['adresseGarage']
        )
        db.session.add(new_garage)
        db.session.commit()
        return jsonify({"message": "Garage créé"}), 201

    if request.method == 'GET':
        garages = Garage.query.all()
        return jsonify([g.to_dict() for g in garages])

@main.route('/garages/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_garage(id):
    garage = Garage.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(garage.to_dict())

    if request.method == 'PUT':
        data = request.get_json()
        garage.nomGarage = data['nomGarage']
        garage.adresseGarage = data['adresseGarage']
        db.session.commit()
        return jsonify({"message": "Garage mis à jour"})

    if request.method == 'DELETE':
        db.session.delete(garage)
        db.session.commit()
        return jsonify({"message": "Garage supprimé"})