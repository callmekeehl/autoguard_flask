# routes/police_routes.py
from flask import Blueprint, request, jsonify
from models.Police import Police
from app import db

police_bp = Blueprint('police_bp', __name__)

@police_bp.route('/polices', methods=['GET', 'POST'])
def handle_polices():
    if request.method == 'POST':
        data = request.get_json()
        new_police = Police(
            nom=data['nom'],
            prenom=data['prenom'],
            email=data['email'],
            adresse=data['adresse'],
            telephone=data['telephone'],
            nomDepartement=data['nomDepartement'],
            adresseDepartement=data['adresseDepartement']
        )
        new_police.motDePasse = data['motDePasse']  # Utilise le setter pour hacher le mot de passe
        db.session.add(new_police)
        db.session.commit()
        return jsonify({"message": "Police créée"}), 201

    if request.method == 'GET':
        polices = Police.query.all()
        return jsonify([p.to_dict() for p in polices])

@police_bp.route('/polices/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_police(id):
    police = Police.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(police.to_dict())

    if request.method == 'PUT':
        data = request.get_json()
        police.nom = data['nom']
        police.prenom = data['prenom']
        police.email = data['email']
        police.adresse = data['adresse']
        police.telephone = data['telephone']
        police.nomDepartement = data['nomDepartement']
        police.adresseDepartement = data['adresseDepartement']
        if 'motDePasse' in data:
            police.motDePasse = data['motDePasse']  # Utilise le setter pour hacher le mot de passe
        db.session.commit()
        return jsonify({"message": "Police mise à jour"})

    if request.method == 'DELETE':
        db.session.delete(police)
        db.session.commit()
        return jsonify({"message": "Police supprimée"})
