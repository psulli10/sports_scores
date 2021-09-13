from models.attribute import Attribute
from models.player import Player
from models.team import Team
from db.run_sql import run_sql
import repositories.player_repository as player_repository

# CREATE
def save(team):
    sql = "INSERT INTO teams (name, wins, draws, defeats) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [team.name, team.wins, team.draws, team.defeats]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team


# READ
def select_all():
    sql = "SELECT * FROM teams"
    teams = []
    results = run_sql(sql)
    for row in results:
        # Need a select players by team id method for here
        players = player_repository.select_all_by_team(row['id'])
        team_attributes = Attribute(row['strength'], row['speed'], row['intelligence'], row['fitness'], row['adaptability'])
        team = Team(row['name'], team_attributes, row['wins'], row['draws'], row['defeats'], players, row['id'])
        teams.append(team)
    return teams

def select(id):
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    # print(result[0])
    team_attributes = Attribute(result['strength'], result['speed'], result['intelligence'], result['fitness'], result['adaptability'])
    players = player_repository.select_all_by_team(id)
    team = Team(result['name'], team_attributes, result['wins'], result['draws'], result['defeats'], players, result['id'])
    return team


# UPDATE
def update(team):
    sql = "UPDATE teams SET (name, strength, speed, intelligence, fitness, adaptability, wins, draws, defeats) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [team.name, team.attributes.strength, team.attributes.speed, team.attributes.intelligence, team.attributes.fitness, team.attributes.adaptability, team.wins, team.draws, team.defeats, team.id]
    run_sql(sql, values)


# DELETE
def delete_all():
    sql = "DELETE  FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)








