from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.astias.models import Astia, ASTIA_COLUMNS
from application.status.models import Status
from application.epic.models import Epic
from application.auth.models import User

@app.route("/astiat", methods=["GET"])
def astias_index():
	return render_template("astias/list.html", astias=Astia.query.all(), statuses=Status.query.all(), epics=Epic.query.all(), users=User.query.all(), counts=User.find_astia_counts())

@app.route("/astiat/<astia_id>/", methods=["GET"])
def astias_show(astia_id: str):
	t: Astia = Astia.query.get(astia_id)
	return render_template("astias/show.html", astia=t, statuses=Status.query.all(), epics=Epic.query.all(), users=User.query.all())

@app.route("/astiat/<astia_id>/poista", methods=["DELETE", "POST"]) # POST sisällytetty HTML-standardin puutteellisuuden vuoksi
def astias_delete(astia_id: str):
	t: Astia = Astia.query.get(astia_id)
	db.session().delete(t)
	db.session().commit()
	return render_template("astias/list.html", astias=Astia.query.all(), statuses=Status.query.all(), epics=Epic.query.all(), users=User.query.all(), counts=User.find_astia_counts()), 400

@app.route("/astiat/<astia_id>/", methods=["PUT", "POST"]) # POST sisällytetty HTML-standardin puutteellisuuden vuoksi
@login_required
def astias_edit(astia_id: str):
	t: Astia = Astia.query.get(astia_id)
	for column in ASTIA_COLUMNS:
		if not column.validate(request.form):
			return render_template("astias/list.html", astias=Astia.query.all(), statuses=Status.query.all(), epics=Epic.query.all(), users=User.query.all(), counts=User.find_astia_counts()), 400
		column.set_from_form(t, request.form)
	
	db.session().commit()

	t = Astia.query.get(astia_id)
	return render_template("astias/show.html", astia=t, statuses=Status.query.all(), epics=Epic.query.all(), users=User.query.all())

@app.route("/astiat/<astia_id>/status", methods=["PUT", "POST"]) # POST sisällytetty HTML-standardin puutteellisuuden vuoksi
@login_required
def astias_set_status(astia_id):
	t: Astia = Astia.query.get(astia_id)
	status: Status = Status.query.get(request.form["status"])
	if not status:
		return redirect(url_for("astias_index")), 400

	t.status = status

	db.session().add(t)
	db.session().commit()

	return redirect(url_for("astias_index"))

@app.route("/astiat/<astia_id>/vastuuhenkilö", methods=["PUT", "POST"]) # POST sisällytetty HTML-standardin puutteellisuuden vuoksi
@login_required
def astias_set_assignee(astia_id):
	t: Astia = Astia.query.get(astia_id)
	user: User = User.query.get(request.form["vastuuhenkilö"])
	if not user:
		return redirect(url_for("astias_index")), 400

	t.assignee = user

	db.session().add(t)
	db.session().commit()

	return redirect(url_for("astias_index"))

@app.route("/astiat/<astia_id>/kokonaisuus", methods=["PUT", "POST"]) # POST sisällytetty HTML-standardin puutteellisuuden vuoksi
@login_required
def astias_set_epics(astia_id):
	t: Astia = Astia.query.get(astia_id)
	print("======================", request.form.getlist("kokonaisuus"))
	t.epics = []
	for epic_id in request.form.getlist("kokonaisuus"):
		epic = Epic.query.get(epic_id)
		if epic:
			t.epics.append(epic)
		else:
			return redirect(url_for("astias_index")), 400

	db.session().add(t)
	db.session().commit()

	return redirect(url_for("astias_index"))

@app.route("/astiat", methods=["POST"])
@login_required
def astias_create():
	t = Astia()
	t.creator_id = current_user.id
	t.assignee_id = current_user.id
	for column in ASTIA_COLUMNS:
		if column.name_fi not in request.form:
			continue
		if not column.validate(request.form):
			return render_template("astias/list.html", astias=Astia.query.all(), statuses=Status.query.all(), epics=Epic.query.all(), users=User.query.all(), counts=User.find_astia_counts()), 400
		column.set_from_form(t, request.form)

	db.session().add(t)
	db.session().commit()

	return redirect(url_for("astias_index"))