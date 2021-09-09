from models.attribute import Attribute
from models.player import Player
from models.team import Team
from db.run_sql import run_sql
import repositories.player_repository as player_repository

def save(team):
    sql = "INSERT INTO teams (name, wins, draws, defeats) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [team.name, team.wins, team.draws, team.defeats]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team

def select_all():
    sql = "SELECT * FROM teams"
    teams = []
    results = run_sql(sql)
    for row in results:
        # Need a select players by team id method for here
        players = player_repository.select_all_by_team(row['id'])
        team = Team(row['name'], players, row['id'])
        teams.append(team)
    return teams

def delete_all():
    sql = "DELETE  FROM teams"
    run_sql(sql)