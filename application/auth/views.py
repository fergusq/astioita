from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.auth.models import User

@app.route("/tunnus/kirjautuminen", methods = ["POST"])
def auth_login():
	user = User.query.filter_by(username=request.form["tunnus"], password=request.form["salasana"]).first()
	if not user:
		return render_template("auth/loginerror.html", error = "Virheellinen tunnus tai salasana"), 403

	login_user(user)
	print("Käyttäjä " + user.name + " tunnistettiin")
	return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
	logout_user()
	return redirect(url_for("index"))