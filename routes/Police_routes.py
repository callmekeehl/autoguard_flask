# routes/police_routes.py
from flask import Blueprint, request, jsonify
from models.Police import Police
from models.Utilisateur import Utilisateur
from app import db

police_bp = Blueprint('police_bp', __name__)


@police_bp.route('/polices', methods=['POST'])
def create_police():
    data = request.get_json()

    # Crée d'abord l'utilisateur de base
    new_user = Utilisateur(
        nom=data['nom'],
        prenom=data['prenom'],
        email=data['email'],
        adresse=data['adresse'],
        telephone=data['telephone'],
        type='police'  # Indique que cet utilisateur est une police
    )
    new_user.motDePasse = data['motDePasse']
    db.session.add(new_user)
    db.session.commit()

    # Ensuite, crée l'entrée spécifique de la police
    new_police = Police(
        utilisateurId=new_user.utilisateurId,
        nomDepartement=data['nomDepartement'],
        adresseDepartement=data['adresseDepartement']
    )
    db.session.add(new_police)
    db.session.commit()

    return jsonify({"message": "Police créée", "policeId": new_police.policeId}), 201


@police_bp.route('/polices', methods=['GET'])
def get_polices():
    polices = Police.query.all()
    return jsonify([p.to_dict() for p in polices])


@police_bp.route('/polices/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_police(id):
    police = Police.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(police.to_dict())

    if request.method == 'PUT':
        data = request.get_json()

        # Mettez à jour les champs de l'utilisateur de base
        utilisateur = Utilisateur.query.get(police.utilisateurId)
        utilisateur.nom = data['nom']
        utilisateur.prenom = data['prenom']
        utilisateur.email = data['email']
        utilisateur.adresse = data['adresse']
        utilisateur.telephone = data['telephone']
        if 'motDePasse' in data:
            utilisateur.motDePasse = data['motDePasse']

        # Mettez à jour les champs spécifiques à la police
        police.nomDepartement = data['nomDepartement']
        police.adresseDepartement = data['adresseDepartement']
        db.session.commit()

        return jsonify({"message": "Police mise à jour"})

    if request.method == 'DELETE':
        # Supprimez d'abord l'entrée de la police
        db.session.delete(police)
        db.session.commit()

        # Ensuite, supprimez l'utilisateur de base
        utilisateur = Utilisateur.query.get(police.utilisateurId)
        db.session.delete(utilisateur)
        db.session.commit()

        return jsonify({"message": "Police supprimée"})
