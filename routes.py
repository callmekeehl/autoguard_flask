# routes.py
from flask import Blueprint, request, jsonify
from models import Declaration, Notification, Rdv, Police, Garage
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
            telephone=data['telephone']
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
            utilisateur.motDePasse = data['motDePasse']  # Utiliser le setter pour hacher le mot de passe
        db.session.commit()
        return jsonify({"message": "Utilisateur mis à jour"})

    if request.method == 'DELETE':
        db.session.delete(utilisateur)
        db.session.commit()
        return jsonify({"message": "Utilisateur supprimé"})


#-----------------------------------------------------------------------------------------------
# Notifications routes
# routes.py
@main.route('/notifications', methods=['GET', 'POST'])
def handle_notifications():
    if request.method == 'POST':
        data = request.get_json()
        new_notification = Notification(
            utilisateurId=data['utilisateurId'],
            message=data['message'],
            dateEnvoi=data['dateEnvoi'],
            lu=data['lu']
        )
        db.session.add(new_notification)
        db.session.commit()
        return jsonify({"message": "Notification créée"}), 201

    if request.method == 'GET':
        notifications = Notification.query.all()
        return jsonify([n.to_dict() for n in notifications])


@main.route('/notifications/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_notification(id):
    notification = Notification.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(notification.to_dict())

    if request.method == 'PUT':
        data = request.get_json()
        notification.utilisateurId = data['utilisateurId']
        notification.message = data['message']
        notification.dateEnvoi = data['dateEnvoi']
        notification.lu = data['lu']
        db.session.commit()
        return jsonify({"message": "Notification mise à jour"})

    if request.method == 'DELETE':
        db.session.delete(notification)
        db.session.commit()
        return jsonify({"message": "Notification supprimée"})


#---------------------------------------------------------------------------
# Déclaration routes
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
            photoCarteGrise=data.get('photoCarteGrise'),  # Peut-être None
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
        declaration.photoCarteGrise = data.get('photoCarteGrise')
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


#----------------------------------------------------------
# Rdv routes

# routes.py
@main.route('/rdvs', methods=['GET', 'POST'])
def handle_rdvs():
    if request.method == 'POST':
        data = request.get_json()
        new_rdv = Rdv(
            utilisateurId=data['utilisateurId'],
            garageId=data['garageId'],
            date=data['date'],
            motif=data['motif']
        )
        db.session.add(new_rdv)
        db.session.commit()
        return jsonify({"message": "Rendez-vous créé"}), 201

    if request.method == 'GET':
        rdvs = Rdv.query.all()
        return jsonify([r.to_dict() for r in rdvs])

@main.route('/rdvs/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_rdv(id):
    rdv = Rdv.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify(rdv.to_dict())

    if request.method == 'PUT':
        data = request.get_json()
        rdv.utilisateurId = data['utilisateurId']
        rdv.garageId = data['garageId']
        rdv.date = data['date']
        rdv.motif = data['motif']
        db.session.commit()
        return jsonify({"message": "Rendez-vous mis à jour"})

    if request.method == 'DELETE':
        db.session.delete(rdv)
        db.session.commit()
        return jsonify({"message": "Rendez-vous supprimé"})

#--------------------------------------------------------------------------------------
# Police routes

# routes.py
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
        return jsonify({"message": "Département de police créé"}), 201

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
        return jsonify({"message": "Département de police mis à jour"})

    if request.method == 'DELETE':
        db.session.delete(police)
        db.session.commit()
        return jsonify({"message": "Département de police supprimé"})

#-------------------------------------------------------------------------------------------------
# Garage routes

# routes.py
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


#---------------------------------------------------------------------------------------------
