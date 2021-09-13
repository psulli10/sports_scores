from models.game import Game
from models.team import Team
import repositories.team_repository as team_repository
from db.run_sql import run_sql

# CREATE
def save(game):
    sql = "INSERT INTO games (home_id, away_id, home_goals, away_goals, result) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [game.home.id, game.away.id, game.home_goals, game.away_goals, game.result['winner']]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id
    return game

# READ
def select_all():
    games = []

    sql = "SELECT * FROM games"
    results = run_sql(sql)

    for row in results:
        home = team_repository.select(row['home_id'])
        away = team_repository.select(row['away_id'])
        game = Game(home, away, row['home_goals'], row['away_goals'], row['id'])
        games.append(game)

    return games    

def select(id):
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    home = team_repository.select(result['home_id'])
    away = team_repository.select(result['away_id'])
    game = Game(home, away, result['home_goals'], result['away_goals'], result['id'])
    return game

# UPDATE
def update(game):
    sql = "UPDATE games SET (home_id, away_id, home_goals, away_goals, result) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [game.home.id, game.away.id, game.home_goals, game.away_goals, game.result['winner'], game.id]
    run_sql(sql, values)


# DELETE
def delete_all():
    sql = "DELETE  FROM games"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)