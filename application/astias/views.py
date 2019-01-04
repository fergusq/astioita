from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.astias.models import Astia, ASTIA_COLUMNS

@app.route("/astiat", methods=["GET"])
def astias_index():
	return render_template("astias/list.html", astias=Astia.query.all())

@app.route("/astiat/<astia_id>/", methods=["GET"])
def astias_show(astia_id: str):
	t: Astia = Astia.query.get(astia_id)
	return render_template("astias/show.html", astia=t)

@app.route("/astiat/<astia_id>/", methods=["POST"])
@login_required
def astias_edit(astia_id: str):
	t: Astia = Astia.query.get(astia_id)
	for column in ASTIA_COLUMNS:
		if not column.validate(request.form):
			return render_template("astias/list.html", astias=Astia.query.all()), 401
		column.set_from_form(t, request.form)
	
	db.session().commit()

	t = Astia.query.get(astia_id)
	return render_template("astias/show.html", astia=t)

@app.route("/astiat/uusi")
def astias_form():
	return render_template("astias/new.html")

@app.route("/astiat", methods=["POST"])
@login_required
def astias_create():
	t = Astia()
	t.creator_id = current_user.id
	for column in ASTIA_COLUMNS:
		if not column.validate(request.form):
			return render_template("astias/list.html", astias=Astia.query.all()), 401
		column.set_from_form(t, request.form)

	db.session().add(t)
	db.session().commit()

	return redirect(url_for("astias_index"))