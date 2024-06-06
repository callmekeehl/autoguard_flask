from datetime import datetime
from app import db


class Utilisateur(db.Model):
    utilisateurId = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    adresse = db.Column(db.String(200), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    motDePasse = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            "utilisateurId": self.utilisateurId,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "adresse": self.adresse,
            "telephone": self.telephone,
            "motDePasse": self.motDePasse
        }