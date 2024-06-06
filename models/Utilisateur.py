# models/utilisateur.py
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Utilisateur(db.Model):
    utilisateurId = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    adresse = db.Column(db.String(200), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    _motDePasse = db.Column('motDePasse', db.String(200), nullable=False)

    @property
    def motDePasse(self):
        raise AttributeError('motDePasse is not a readable attribute')

    @motDePasse.setter
    def motDePasse(self, password):
        self.motDePasse = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.motDePasse, password)

    def to_dict(self):
        return {
            "utilisateurId": self.utilisateurId,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "adresse": self.adresse,
            "telephone": self.telephone,
        }
