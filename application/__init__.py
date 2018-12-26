from flask import Flask
app = Flask(__name__)

from flaskext.markdown import Markdown
Markdown(app)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///astiatietokanta.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

from application import views
from application.astias import models, views

db.create_all()