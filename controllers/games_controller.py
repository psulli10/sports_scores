from flask import Flask, Blueprint, render_template, redirect, request
import repositories.game_repository as game_repository

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def index():
	games = game_repository.select_all()
	return render_template("/games/index.html", games=games)