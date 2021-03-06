import os

from flask import Flask

app = Flask(__name__)

from flaskext.markdown import Markdown

Markdown(app)

if os.environ.get("HEROKU"):
	app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
	app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///astiatietokanta.db"
	app.config["SQLALCHEMY_ECHO"] = True

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

app.config["SECRET_KEY"] = os.urandom(32)

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään käyttääksesi tätä ominaisuutta."

from application import views
import application.astias.models
import application.astias.views
import application.auth.models
import application.auth.views
import application.status.models
import application.status.views
import application.epic.models
import application.epic.views


@login_manager.user_loader
def load_user(user_id: int):
	return application.auth.models.User.query.get(user_id)


db.create_all()
