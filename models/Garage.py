# models/garage.py
from app import db
from models.Utilisateur import Utilisateur


class Garage(Utilisateur):
    __tablename__ = 'garages'
    __mapper_args__ = {
        'polymorphic_identity': 'garage',
        'inherit_condition': (db.ForeignKey('utilisateurs.utilisateurId') == db.column('garages.garageId'))
    }

    garageId = db.Column(db.Integer, db.ForeignKey('utilisateurs.utilisateurId'), primary_key=True)
    nomGarage = db.Column(db.String(100), nullable=False)
    adresseGarage = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "garageId": self.garageId,
            "nomGarage": self.nomGarage,
            "adresseGarage": self.adresseGarage
        })
        return data
