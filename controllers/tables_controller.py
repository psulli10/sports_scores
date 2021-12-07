from flask import Flask, Blueprint, render_template, redirect, request
import repositories.team_repository as table_repository

tables_blueprint = Blueprint("tables", __name__)

@tables_blueprint.route("/table")
def index():
	tables = table_repository.select_all()
	return render_template("/tables/index.html")