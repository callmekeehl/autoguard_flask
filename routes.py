# routes.py
from flask import Blueprint, request, jsonify

from models import Declaration
from models.Utilisateur import Utilisateur
from app import db

main = Blueprint('main', __name__)

# Utilisateur routes
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
        )
        new_user.motDePasse = data['motDePasse']
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
        if 'motDePasse' in data:
            utilisateur.motDePasse_hash = data['motDePasse']
        db.session.commit()
        return jsonify({"message": "Utilisateur mis à jour"})

    if request.method == 'DELETE':
        db.session.delete(utilisateur)
        db.session.commit()
        return jsonify({"message": "Utilisateur supprimé"})


# Declaration routes
@main.route('/declarations', methods=['GET', 'POST'])
def handle_declarations():
    if request.method == 'POST':
        data = request.get_json()
        new_declaration = Declaration(
            utilisateurId=data['utilisateurId'],
            nomProprio=data['nomProprio'],
            prenomProprio=data['prenomProprio'],
            telephoneProprio=data['telephoneProprio'],
            lieuLong=data['lieuLong'],
            lieuLat=data['lieuLat'],
            photoCarteGrise=data['photoCarteGrise'],
            numChassis=data['numChassis'],
            numPlaque=data['numPlaque'],
            marque=data['marque'],
            modele=data['modele'],
            dateHeure=data['dateHeure'],
            statut=data['statut']
        )
        db.session.add(new_declaration)
        db.session.commit()
        return jsonify({"message": "Déclaration créée"}), 201

    if request.method == 'GET':
        declarations = Declaration.query.all()
        return jsonify([d.to_dict() for d in declarations])

@main.route('/declarations/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_declaration(id):
    declaration = Declaration.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(declaration.to_dict())

    if request.method == 'PUT':
        data = request.get_json()
        declaration.utilisateurId = data['utilisateurId']
        declaration.nomProprio = data['nomProprio']
        declaration.prenomProprio = data['prenomProprio']
        declaration.telephoneProprio = data['telephoneProprio']
        declaration.lieuLong = data['lieuLong']
        declaration.lieuLat = data['lieuLat']
        declaration.photoCarteGrise = data['photoCarteGrise']
        declaration.numChassis = data['numChassis']
        declaration.numPlaque = data['numPlaque']
        declaration.marque = data['marque']
        declaration.modele = data['modele']
        declaration.dateHeure = data['dateHeure']
        declaration.statut = data['statut']
        db.session.commit()
        return jsonify({"message": "Déclaration mise à jour"})

    if request.method == 'DELETE':
        db.session.delete(declaration)
        db.session.commit()
        return jsonify({"message": "Déclaration supprimée"})