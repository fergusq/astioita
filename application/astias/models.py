from flask_sqlalchemy import sqlalchemy as sa
from application import db

class AstiaColumn:
	def __init__(self, name_en: str, name_fi: str):
		self.name_en = name_en
		self.name_fi = name_fi
	
	def set_from_form(self, astia: "Astia", form):
		str_rep = form.get(self.name_fi)
		setattr(astia, self.name_en, str_rep)

ASTIA_COLUMNS = [
	AstiaColumn("title", "otsikko"),
	AstiaColumn("description", "kuvaus"),
]

class Astia(db.Model):
	id = sa.Column(sa.Integer, primary_key=True)
	date_created = sa.Column(sa.DateTime, default=sa.func.current_timestamp())
	date_modified = sa.Column(sa.DateTime, default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp())

	title = sa.Column(sa.Text(), nullable=False)
	description = sa.Column(sa.Text(), nullable=False)

	def __init__(self):
		pass