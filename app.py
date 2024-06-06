# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://justkeehl:justkeehl2003@localhost/autoguard'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importez vos modèles ici après la configuration de la base de données
from models.Utilisateur import Utilisateur
from models.Notification import Notification
from models.Declaration import Declaration
from models.Police import Police
from models.Garage import Garage
from models.Rdv import Rdv

# Importez et enregistrez les blueprints des routes
from routes import main as main_blueprint
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
