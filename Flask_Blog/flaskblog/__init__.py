import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

#Imported a randomly generated seceret key using import secrets 

app.config['SECRET_KEY'] = 'afc48752f0fd9292ddc603a09a25f65e'

#Using SQLite I set a relative path to the database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#Database instance

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#Login manager configirations

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#Flask mail configirations

app.config['MAIL_SERVER'] = 'smtp.googleemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


from flaskblog import routes
