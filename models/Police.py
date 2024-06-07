# models/Police.py
from app import db
from models.Utilisateur import Utilisateur


class Police(db.Model):
    __tablename__ = 'police'
    policeId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    utilisateurId = db.Column(db.Integer, db.ForeignKey('utilisateur.utilisateurId'), nullable=False)
    utilisateur = db.relationship('Utilisateur', backref=db.backref('police', uselist=False))
    nomDepartement = db.Column(db.String(100), nullable=False)
    adresseDepartement = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            "policeId": self.policeId,
            "utilisateurId": self.utilisateurId,
            "nomDepartement": self.nomDepartement,
            "adresseDepartement": self.adresseDepartement,
            "nom": self.utilisateur.nom,
            "prenom": self.utilisateur.prenom,
            "email": self.utilisateur.email,
            "adresse": self.utilisateur.adresse,
            "telephone": self.utilisateur.telephone
        }
