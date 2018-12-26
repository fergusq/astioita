from flask import redirect, render_template, request, url_for

from application import app, db
from application.astias.models import Astia, ASTIA_COLUMNS

@app.route("/astiat", methods=["GET"])
def astias_index():
	return render_template("astias/list.html", astias=Astia.query.all())

@app.route("/astiat/<astia_id>/", methods=["GET"])
def astias_show(astia_id):
	t = Astia.query.get(astia_id)
	return render_template("astias/show.html", astia=t)

@app.route("/astiat/<astia_id>/", methods=["POST"])
def astias_edit(astia_id):
	t = Astia.query.get(astia_id)
	for column in ASTIA_COLUMNS:
		column.set_from_form(t, request.form)
	
	db.session().commit()

	t = Astia.query.get(astia_id)
	return render_template("astias/show.html", astia=t)

@app.route("/astiat/uusi")
def astias_form():
	return render_template("astias/new.html")

@app.route("/astiat", methods=["POST"])
def astias_create():
	t = Astia()
	for column in ASTIA_COLUMNS:
		column.set_from_form(t, request.form)

	db.session().add(t)
	db.session().commit()

	return redirect(url_for("astias_index"))