# models/Garage.py
from app import db
from models.Utilisateur import Utilisateur


class Garage(db.Model):
    __tablename__ = 'garage'
    garageId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    utilisateurId = db.Column(db.Integer, db.ForeignKey('utilisateur.utilisateurId'), nullable=False)
    utilisateur = db.relationship('Utilisateur', backref=db.backref('garage', uselist=False))
    nomGarage = db.Column(db.String(100), nullable=False)
    adresseGarage = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            "garageId": self.garageId,
            "utilisateurId": self.utilisateurId,
            "nomGarage": self.nomGarage,
            "adresseGarage": self.adresseGarage,
            "nom": self.utilisateur.nom,
            "prenom": self.utilisateur.prenom,
            "email": self.utilisateur.email,
            "adresse": self.utilisateur.adresse,
            "telephone": self.utilisateur.telephone
        }
