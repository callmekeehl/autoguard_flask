from app import db


class Police(db.Model):
    policeId = db.Column(db.Integer, primary_key=True)
    nomDepartement = db.Column(db.String(100), nullable=False)
    adresseDepartement = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            "policeId": self.policeId,
            "nomDepartement": self.nomDepartement,
            "adresseDepartement": self.adresseDepartement,
        }