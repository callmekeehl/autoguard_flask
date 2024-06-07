from flask import Blueprint, request, jsonify
from models import Declaration, Notification, Rdv, Police, Garage
from models.Utilisateur import Utilisateur
from app import db

main = Blueprint('main', __name__)

# routes.py (ajoutez ce code à la suite de celui existant)
from models.Police import Police

@main.route('/polices', methods=['GET', 'POST'])
def handle_polices():
    if request.method == 'POST':
        data = request.get_json()
        new_police = Police(
            nomDepartement=data['nomDepartement'],
            adresseDepartement=data['adresseDepartement']
        )
        db.session.add(new_police)
        db.session.commit()
        return jsonify({"message": "Police créée"}), 201

    if request.method == 'GET':
        polices = Police.query.all()
        return jsonify([p.to_dict() for p in polices])

@main.route('/polices/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_police(id):
    police = Police.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(police.to_dict())

    if request.method == 'PUT':
        data = request.get_json()
        police.nomDepartement = data['nomDepartement']
        police.adresseDepartement = data['adresseDepartement']
        db.session.commit()
        return jsonify({"message": "Police mise à jour"})

    if request.method == 'DELETE':
        db.session.delete(police)
        db.session.commit()
        return jsonify({"message": "Police supprimée"})
