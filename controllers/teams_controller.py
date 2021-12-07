from flask import Flask, Blueprint, render_template, redirect, request
import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def index():
	teams = team_repository.select_all()
	return render_template("/teams/index.html", teams=teams)