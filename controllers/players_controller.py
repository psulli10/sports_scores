from flask import Flask, Blueprint, render_template, redirect, request
import repositories.player_repository as player_repository

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/players")
def index():
    players = player_repository.select_all()
    return render_template("players/index.html", title = "Scores - Players", players = players)
