from app import db


class Garage(db.Model):
    garageId = db.Column(db.Integer, primary_key=True)
    nomGarage = db.Column(db.String(100), nullable=False)
    adresseGarage = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            "garageId": self.garageId,
            "nomGarage": self.nomGarage,
            "adresseGarage": self.adresseGarage,
        }