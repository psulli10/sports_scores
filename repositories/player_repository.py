from models.attribute import Attribute
from models.player import Player
from db.run_sql import run_sql
import repositories.team_repository as team_repository


# CREATE
def save(player):
    sql = "INSERT INTO players (name, squad_number, position, strength, speed, intelligence, fitness, adaptability, team_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [player.name, player.squad_number, player.position, player.attributes.strength, player.attributes.speed, player.attributes.intelligence, player.attributes.fitness, player.attributes.adaptability, player.team.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player


# READ
def select_all():
    sql = "SELECT * FROM players"
    players = []
    results = run_sql(sql)
    for row in results:
        attributes = Attribute(row['strength'], row['speed'], row['intelligence'], row['fitness'], row['adaptability'])
        team = team_repository.select(row['team_id'])
        player = Player(row['name'], attributes, row['squad_number'], row['position'], team, row['id'])
        players.append(player)

    return players

def select(id):
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    attributes = Attribute(result['strength'], result['speed'], result['intelligence'], result['fitness'], result['adaptability'])
    team = team_repository.select(result['team_id'])
    player = Player(result['name'], attributes, result['squad_number'], result['position'], team, result['id'])
    return player



def select_all_by_team(team_id):
    sql = "SELECT * FROM players WHERE team_id = %s"
    values = [team_id]
    players = []
    results = run_sql(sql, values)
    for row in results:
        attributes = Attribute(row['strength'], row['speed'], row['intelligence'], row['fitness'], row['adaptability'])
        player = Player(row['name'], attributes, row['squad_number'], row['position'], row['id'])
        players.append(player)

    return players

# UPDATE

def update(player):
    sql = "UPDATE players SET (name, squad_number, position, strength, speed, intelligence, fitness, adaptability, team_id) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [player.name, player.squad_number, player.position, player.attributes.strength, player.attributes.speed, player.attributes.intelligence, player.attributes.fitness, player.attributes.adaptability, player.team.id, player.id]
    run_sql(sql, values)

# DELETE

def delete_all():
    sql = "DELETE  FROM players"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)