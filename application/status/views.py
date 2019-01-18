from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.status.models import Status, STATUS_COLUMNS
from application.auth.models import User


@app.route("/statukset", methods=["GET"])
def statuses_index():
	return render_template("status/list.html", statuses=Status.query.all())

@app.route("/statukset/<status_id>/", methods=["GET"])
def statuses_show(status_id: str):
	t: Status = Status.query.get(status_id)
	return render_template("status/show.html", status=t, statuses=Status.query.all())

@app.route("/statukset/<status_id>/muokkaa", methods=["GET"])
def statuses_edit(status_id: str):
	t: Status = Status.query.get(status_id)
	return render_template("status/edit.html", status=t, statuses=Status.query.all())

@app.route("/statukset/<status_id>/", methods=["DELETE", "POST"]) # POST sisällytetty HTML-standardin puutteellisuuden vuoksi
def statuses_delete(status_id: str):
	t: Status = Status.query.get(status_id)
	db.session().delete(t)
	db.session().commit()
	return render_template("status/list.html", statuses=Status.query.all()), 400

@app.route("/statukset/<status_id>/poista", methods=["PUT", "POST"]) # POST sisällytetty HTML-standardin puutteellisuuden vuoksi
@login_required
def statuses_delete(status_id: str):
	t: Status = Status.query.get(status_id)
	for column in STATUS_COLUMNS:
		if not column.validate(request.form):
			return render_template("statuses/list.html", statuses=Status.query.all()), 400
		column.set_from_form(t, request.form)
	
	db.session().commit()

	t = Status.query.get(status_id)
	return render_template("status/show.html", status=t, statuses=Status.query.all())

@app.route("/statukset", methods=["POST"])
@login_required
def statuses_create():
	t = Status()
	for column in STATUS_COLUMNS:
		if not column.validate(request.form):
			return render_template("statuses/list.html", statuses=Status.query.all()), 400
		column.set_from_form(t, request.form)

	db.session().add(t)
	db.session().commit()

	return redirect(url_for("statuses_index"))