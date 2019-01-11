from flask_sqlalchemy import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.sql import text

from application import db
from application.columns import Column, NonEmptyString
from application.astias.models import Astia

class User(db.Model):
	__tablename__ = "account"

	id = sa.Column(sa.Integer, primary_key=True)
	date_created = sa.Column(sa.DateTime, default=sa.func.current_timestamp())
	date_modified = sa.Column(sa.DateTime, default=sa.func.current_timestamp(), onupdate=sa.func.current_timestamp())

	name = sa.Column(sa.Text(), nullable=False)
	username = sa.Column(sa.Text(), nullable=False)
	password = sa.Column(sa.Text(), nullable=False)

	created_astias = orm.relationship("Astia", backref="creator", foreign_keys=[Astia.creator_id], lazy=True)
	assigned_astias = orm.relationship("Astia", backref="assignee", foreign_keys=[Astia.assignee_id], lazy=True)

	def __init__(self) -> None:
		pass
	
	def get_id(self) -> int:
		return self.id
	
	def is_active(self) -> bool:
		return True
	
	def is_anonymous(self) -> bool:
		return False
	
	def is_authenticated(self) -> bool:
		return True
	
	@staticmethod
	def find_astia_counts() -> list:
		stmt = text("""
		SELECT account.id, account.name, COUNT(astia.id) AS astia_count
		FROM account
		LEFT JOIN astia
		ON astia.assignee_id = account.id
		GROUP BY account.id
		ORDER BY astia_count;
		""")
		res = db.engine.execute(stmt)

		ans = []
		for r in res:
			ans.append({"id": r[0], "name": r[1], "count": r[2]})

		return ans

USER_COLUMNS = [
	Column("name", "nimi", NonEmptyString),
	Column("username", "tunnus", NonEmptyString),
	Column("password", "salasana", lambda _x: True),
]