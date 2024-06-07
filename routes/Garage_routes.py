# routes/garage_routes.py
from flask import Blueprint, request, jsonify
from models.Garage import Garage
from models.Utilisateur import Utilisateur
from app import db

garage_bp = Blueprint('garage_bp', __name__)


@garage_bp.route('/garages', methods=['POST'])
def create_garage():
    data = request.get_json()

    # Crée d'abord l'utilisateur de base
    new_user = Utilisateur(
        nom=data['nom'],
        prenom=data['prenom'],
        email=data['email'],
        adresse=data['adresse'],
        telephone=data['telephone'],
        type='garage'  # Indique que cet utilisateur est un garage
    )
    new_user.motDePasse = data['motDePasse']
    db.session.add(new_user)
    db.session.commit()

    # Ensuite, crée l'entrée spécifique du garage
    new_garage = Garage(
        utilisateurId=new_user.utilisateurId,
        nomGarage=data['nomGarage'],
        adresseGarage=data['adresseGarage']
    )
    db.session.add(new_garage)
    db.session.commit()

    return jsonify({"message": "Garage créé", "garageId": new_garage.garageId}), 201


@garage_bp.route('/garages', methods=['GET'])
def get_garages():
    garages = Garage.query.all()
    return jsonify([g.to_dict() for g in garages])


@garage_bp.route('/garages/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_garage(id):
    garage = Garage.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(garage.to_dict())

    if request.method == 'PUT':
        data = request.get_json()

        # Mettez à jour les champs de l'utilisateur de base
        utilisateur = Utilisateur.query.get(garage.utilisateurId)
        utilisateur.nom = data['nom']
        utilisateur.prenom = data['prenom']
        utilisateur.email = data['email']
        utilisateur.adresse = data['adresse']
        utilisateur.telephone = data['telephone']
        if 'motDePasse' in data:
            utilisateur.motDePasse = data['motDePasse']

        # Mettez à jour les champs spécifiques du garage
        garage.nomGarage = data['nomGarage']
        garage.adresseGarage = data['adresseGarage']
        db.session.commit()

        return jsonify({"message": "Garage mis à jour"})

    if request.method == 'DELETE':
        # Supprimez d'abord l'entrée du garage
        db.session.delete(garage)
        db.session.commit()

        # Ensuite, supprimez l'utilisateur de base
        utilisateur = Utilisateur.query.get(garage.utilisateurId)
        db.session.delete(utilisateur)
        db.session.commit()

        return jsonify({"message": "Garage supprimé"})
