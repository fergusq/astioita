from typing import Optional

from flask_sqlalchemy import sqlalchemy as sa
from application import db
from application.columns import Column, NonEmptyString

import re

class Astia(db.Model):
	id = sa.Column(sa.Integer, primary_key=True)
	date_created = sa.Column(sa.DateTime, default=sa.func.current_timestamp())
	date_modified = sa.Column(sa.DateTime, default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp())

	title = sa.Column(sa.Text(), nullable=False)
	description = sa.Column(sa.Text(), nullable=False)

	creator_id = sa.Column(sa.Integer, sa.ForeignKey('account.id'), nullable=False)

	def __init__(self) -> None:
		pass

ASTIA_COLUMNS = [
	Column("title", "otsikko", NonEmptyString),
	Column("description", "kuvaus", lambda _x: True),
]