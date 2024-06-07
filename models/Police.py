# models/Police.py
from app import db
from models.Utilisateur import Utilisateur


class Police(Utilisateur):
    policeId = db.Column(db.Integer, primary_key=True)
    nomDepartement = db.Column(db.String(100), nullable=False)
    adresseDepartement = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            "policeId": self.policeId,
            "nomDepartement": self.nomDepartement,
            "adresseDepartement": self.adresseDepartement,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "adresse": self.adresse,
            "telephone": self.telephone
        }
