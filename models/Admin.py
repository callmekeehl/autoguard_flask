from app import db


class Admin(db.Model):
    adminId = db.Column(db.Integer, primary_key=True)

    def to_dict(self):
        return {
            "adminId": self.adminId,
        }
