from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

# Get all of our configuration variables from our config module
app.config.from_object(Config)

# Initialize login and session management
login = LoginManager(app)
login.login_view = 'login' # Here 'login' refers to the endpoint handles logins

# Setup database and flask-migration
db = SQLAlchemy(app)
migate = Migrate(app, db)

# app in this case is our package folder and not the variable above
# The variable above is an instance of flask
from app import routes, models, errors
