from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User, USER_COLUMNS

@app.route("/tunnus/rekisteröityminen", methods=["GET"])
def auth_new():
	return render_template("auth/register.html")

@app.route("/tunnus", methods=["POST"])
def auth_create():
	t = User()
	for column in USER_COLUMNS:
		if not column.validate(request.form):
			return render_template("auth/loginerror.html", error = "Tunnus tai nimi eivät saa olal tyhjiä"), 400
		column.set_from_form(t, request.form)

	db.session().add(t)
	db.session().commit()

	return redirect(url_for("index"))

@app.route("/tunnus/kirjautuminen", methods = ["POST"])
def auth_login():
	user = User.query.filter_by(username=request.form["tunnus"], password=request.form["salasana"]).first()
	if not user:
		return render_template("auth/loginerror.html", error = "Virheellinen tunnus tai salasana"), 403

	login_user(user)
	print("Käyttäjä " + user.name + " tunnistettiin")
	return redirect(url_for("index"))


@app.route("/tunnus/uloskirjautuminen")
def auth_logout():
	logout_user()
	return redirect(url_for("index"))