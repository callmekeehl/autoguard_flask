# models/admin.py
from app import db
from models.Utilisateur import Utilisateur


class Admin(Utilisateur):  # Admin hérite de Utilisateur
    adminId = db.Column(db.Integer, primary_key=True)

    def to_dict(self):
        return {
            "adminId": self.adminId,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "adresse": self.adresse,
            "telephone": self.telephone
        }
