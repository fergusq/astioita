from typing import Optional

from flask_sqlalchemy import sqlalchemy as sa
from sqlalchemy import orm
from application import db
from application.columns import Column, NonEmptyString
from application.auth.models import User

import re

class Astia(db.Model):
	id = sa.Column(sa.Integer, primary_key=True)
	date_created = sa.Column(sa.DateTime, default=sa.func.current_timestamp())
	date_modified = sa.Column(sa.DateTime, default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp())

	title = sa.Column(sa.Text(), nullable=False)
	description = sa.Column(sa.Text(), nullable=False)

	creator_id = sa.Column(sa.Integer, sa.ForeignKey("account.id"), nullable=False)
	assignee_id = sa.Column(sa.Integer, sa.ForeignKey("account.id"), nullable=True)
	status_id = sa.Column(sa.Integer, sa.ForeignKey("status.id"), nullable=False, default=0)

	def __init__(self) -> None:
		pass

ASTIA_COLUMNS = [
	Column("title", "otsikko", NonEmptyString),
	Column("description", "kuvaus", lambda _x: True),
]