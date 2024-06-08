# models/admin.py
from app import db
from models.Utilisateur import Utilisateur


class Admin(Utilisateur):
    __tablename__ = 'admin'
    adminId = db.Column(db.Integer, db.ForeignKey('utilisateur.utilisateurId'), primary_key=True)
    champSpecifiqueAdmin = db.Column(db.String(100))  # Exemple de champ spécifique

    __mapper_args__ = {
        'polymorphic_identity': 'admin',
        'inherit_condition': (adminId == Utilisateur.utilisateurId)
    }

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "adminId": self.adminId,
            "champSpecifiqueAdmin": self.champSpecifiqueAdmin
        })
        return data
