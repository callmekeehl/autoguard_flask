# models/police.py
from app import db
from models.Utilisateur import Utilisateur


class Police(Utilisateur):
    __tablename__ = 'police'
    policeId = db.Column(db.Integer, db.ForeignKey('utilisateur.utilisateurId'), primary_key=True)
    nomDepartement = db.Column(db.String(100), nullable=False)
    adresseDepartement = db.Column(db.String(200), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'police',
        'inherit_condition': (policeId == Utilisateur.utilisateurId)
    }

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "policeId": self.policeId,
            "nomDepartement": self.nomDepartement,
            "adresseDepartement": self.adresseDepartement
        })
        return data
