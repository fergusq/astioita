from flask_sqlalchemy import sqlalchemy as sa
from sqlalchemy import orm

from application import db
from application.columns import Column, NonEmptyString

class User(db.Model):
	__tablename__ = "account"

	id = sa.Column(sa.Integer, primary_key=True)
	date_created = sa.Column(sa.DateTime, default=sa.func.current_timestamp())
	date_modified = sa.Column(sa.DateTime, default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp())

	name = sa.Column(sa.Text(), nullable=False)
	username = sa.Column(sa.Text(), nullable=False)
	password = sa.Column(sa.Text(), nullable=False)

	created_astias = orm.relationship("Astia", backref="creator", lazy=True)

	def __init__(self) -> None:
		pass
	
	def get_id(self):
		return self.id
	
	def is_active(self):
		return True
	
	def is_anonymous(self):
		return False
	
	def is_authenticated(self):
		return True

USER_COLUMNS = [
	Column("name", "nimi", NonEmptyString),
	Column("username", "tunnus", NonEmptyString),
	Column("password", "salasana", lambda _x: True),
]