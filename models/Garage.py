# models/garage.py
from app import db
from models.Utilisateur import Utilisateur


class Garage(Utilisateur):
    __tablename__ = 'garage'
    garageId = db.Column(db.Integer, db.ForeignKey('utilisateur.utilisateurId'), primary_key=True)
    nomGarage = db.Column(db.String(100), nullable=False)
    adresseGarage = db.Column(db.String(200), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'garage',
        'inherit_condition': (garageId == Utilisateur.utilisateurId)
    }

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "garageId": self.garageId,
            "nomGarage": self.nomGarage,
            "adresseGarage": self.adresseGarage
        })
        return data
