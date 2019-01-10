from typing import Optional

from flask_sqlalchemy import sqlalchemy as sa
from sqlalchemy import orm
from application import db
from application.columns import Column, NonEmptyString
from application.auth.models import User

import re

class Status(db.Model):
	id = sa.Column(sa.Integer, primary_key=True)
	date_created = sa.Column(sa.DateTime, default=sa.func.current_timestamp())
	date_modified = sa.Column(sa.DateTime, default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp())

	name = sa.Column(sa.Text(), nullable=False)

	astias = orm.relationship("Astia", backref="status", lazy=True)

	def __init__(self) -> None:
		pass

STATUS_COLUMNS = [
	Column("name", "nimi", NonEmptyString),
]