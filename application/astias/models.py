from flask_sqlalchemy import sqlalchemy as sa
from application import db

class Astia(db.Model):
	id = sa.Column(sa.Integer, primary_key=True)
	date_created = sa.Column(sa.DateTime, default=sa.func.current_timestamp())
	date_modified = sa.Column(sa.DateTime, default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp())

	title = sa.Column(sa.Text(), nullable=False)
	description = sa.Column(sa.Text(), nullable=False)

	def __init__(self, title, desc):
		self.title = title
		self.description = desc