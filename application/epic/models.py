from typing import Optional

from flask_sqlalchemy import sqlalchemy as sa
from sqlalchemy import orm
from application import db
from application.columns import Column, NonEmptyString
from application.auth.models import User

import re

association_table = sa.Table("EpicAstia", db.Model.metadata,
    sa.Column("epic_id", sa.Integer, sa.ForeignKey("epic.id")),
    sa.Column("astia_id", sa.Integer, sa.ForeignKey("astia.id"))
)

class Epic(db.Model):
	id = sa.Column(sa.Integer, primary_key=True)
	date_created = sa.Column(sa.DateTime, default=sa.func.current_timestamp())
	date_modified = sa.Column(sa.DateTime, default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp())

	name = sa.Column(sa.Text(), nullable=False)

	astias = orm.relationship("Astia", secondary=association_table, backref="epics")

	def __init__(self) -> None:
		pass

EPIC_COLUMNS = [
	Column("name", "nimi", NonEmptyString),
]