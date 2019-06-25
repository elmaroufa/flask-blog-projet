from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app= Flask(__name__)
app.config['SECRET_KEY'] = '86cafed16746f23c5856d8529d963161exit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
login_manager = LoginManager(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
from app import models,routes