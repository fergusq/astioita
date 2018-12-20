from flask import redirect, render_template, request, url_for

from application import app, db
from application.astias.models import Astia

@app.route("/astiat", methods=["GET"])
def astias_index():
	return render_template("astias/list.html", astias=Astia.query.all())

@app.route("/astiat/uusi")
def astias_form():
	return render_template("astias/new.html")

@app.route("/astiat", methods=["POST"])
def astias_create():
	t = Astia(request.form.get("otsikko"), request.form.get("kuvaus"))
	db.session().add(t)
	db.session().commit()

	return redirect(url_for("astias_index"))