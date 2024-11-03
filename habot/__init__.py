import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key_here'
app.config['SECRET_KEY'] = 'your_flask_secret_key_here'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir+'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)
jwt = JWTManager(app)

from habot import views