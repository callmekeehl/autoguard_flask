# models/Admin.py
from app import db
from models.Utilisateur import Utilisateur


class Admin(db.Model):
    __tablename__ = 'admin'
    adminId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    utilisateurId = db.Column(db.Integer, db.ForeignKey('utilisateur.utilisateurId'), nullable=False)
    utilisateur = db.relationship('Utilisateur', backref=db.backref('admin', uselist=False))

    def to_dict(self):
        return {
            "adminId": self.adminId,
            "utilisateurId": self.utilisateurId,
            "nom": self.utilisateur.nom,
            "prenom": self.utilisateur.prenom,
            "email": self.utilisateur.email,
            "adresse": self.utilisateur.adresse,
            "telephone": self.utilisateur.telephone
        }
