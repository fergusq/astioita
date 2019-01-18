from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.epic.models import Epic, EPIC_COLUMNS
from application.auth.models import User


@app.route("/kokonaisuudet", methods=["GET"])
def epics_index():
	return render_template("epic/list.html", epics=Epic.query.all())

@app.route("/kokonaisuudet/<epic_id>/", methods=["GET"])
def epics_show(epic_id: str):
	t: Epic = Epic.query.get(epic_id)
	return render_template("epic/show.html", epic=t, epics=Epic.query.all())

@app.route("/kokonaisuudet/<epic_id>/", methods=["DELETE", "POST"]) # POST sisällytetty HTML-standardin puutteellisuuden vuoksi
def epics_delete(epic_id: str):
	t: Epic = Epic.query.get(epic_id)
	db.session().delete(t)
	db.session().commit()
	return render_template("epic/list.html", epics=Epic.query.all()), 400

@app.route("/kokonaisuudet/<epic_id>/poista", methods=["PUT", "POST"]) # POST sisällytetty HTML-standardin puutteellisuuden vuoksi
@login_required
def epics_edit(epic_id: str):
	t: Epic = Epic.query.get(epic_id)
	for column in EPIC_COLUMNS:
		if not column.validate(request.form):
			return render_template("epics/list.html", epics=Epic.query.all()), 400
		column.set_from_form(t, request.form)
	
	db.session().commit()

	t = Epic.query.get(epic_id)
	return render_template("epic/show.html", epic=t, epics=Epic.query.all())

@app.route("/kokonaisuudet", methods=["POST"])
@login_required
def epics_create():
	t = Epic()
	for column in EPIC_COLUMNS:
		if not column.validate(request.form):
			return render_template("epics/list.html", epics=Epic.query.all()), 400
		column.set_from_form(t, request.form)

	db.session().add(t)
	db.session().commit()

	return redirect(url_for("epics_index"))