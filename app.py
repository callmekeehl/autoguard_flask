# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://justkeehl:justkeehl2003@localhost/autoguard_shema'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


# Importation des modèles
from models import Utilisateur, Notification, Declaration, Police, Garage, Admin

# Enregistrement des blueprints
from routes import register_blueprints
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
