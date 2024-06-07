# models/utilisateur.py
from sqlalchemy.orm import relationship

from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'
    utilisateurId = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    adresse = db.Column(db.String(200), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    motDePasse_hash = db.Column(db.String(200), nullable=False)  # Utiliser un nom de colonne différent pour le stockage

    # Cela permettra à SQLAlchemy de savoir que cette classe est la classe parent pour l'héritage
    # Relationships to sub-classes
    admin = relationship("Admin", uselist=False, back_populates="utilisateur")
    garage = relationship("Garage", uselist=False, back_populates="utilisateur")
    police = relationship("Police", uselist=False, back_populates="utilisateur")

    @property
    def motDePasse(self):
        raise AttributeError('motDePasse is not a readable attribute')

    @motDePasse.setter
    def motDePasse(self, password):
        self.motDePasse_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.motDePasse_hash, password)

    def to_dict(self):
        return {
            "utilisateurId": self.utilisateurId,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "adresse": self.adresse,
            "telephone": self.telephone,
        }
