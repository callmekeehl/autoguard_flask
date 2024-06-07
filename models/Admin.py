# models/admin.py
from app import db
from models.Utilisateur import Utilisateur


class Admin(Utilisateur):
    __tablename__ = 'admins'
    __mapper_args__ = {
        'polymorphic_identity': 'admin',
        'inherit_condition': (db.ForeignKey('utilisateurs.utilisateurId') == db.column('admins.adminId'))
    }

    adminId = db.Column(db.Integer, db.ForeignKey('utilisateurs.utilisateurId'), primary_key=True)
    champSpecifiqueAdmin = db.Column(db.String(100))  # Exemple de champ spécifique

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "adminId": self.adminId,
            "champSpecifiqueAdmin": self.champSpecifiqueAdmin
        })
        return data
