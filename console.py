import pdb
from models.attribute import Attribute
from models.player import Player
from models.team import Team
from models.game import Game
import repositories.player_repository as player_repository
import repositories.team_repository as team_repository
import repositories.game_repository as game_repository

# DELETE
player_repository.delete_all()
team_repository.delete_all()
game_repository.delete_all()


# CREATE
player_attributes_1 = Attribute(10, 10, 10, 10, 10)
player_attributes_2 = Attribute(5, 5, 5, 5, 5)
team_attributes_1 = Attribute(8, 8, 8, 8, 8)
team_attributes_2 = Attribute(4, 4, 4, 4, 4)

team_1 = Team("St Mirren", team_attributes_1)
team_repository.save(team_1)
team_2 = Team("Greenock Morton", team_attributes_2)
team_repository.save(team_2)

player_1 = Player("Jamie McGrath", player_attributes_1, 7, "Midfielder", team_1)
player_repository.save(player_1)
player_2 = Player("Marko Rajamaki", player_attributes_2, 9, "Attacker", team_2)
player_repository.save(player_2)

game_1 = Game(team_1, team_2, 3, 0)
print(game_1.result)
game_repository.save(game_1)

# UPDATE 
player_1.squad_number = 10
player_repository.update(player_1)
team_1.wins = 1
team_repository.update(team_1)
game_1.away_goals = 1
game_repository.update(game_1)



player_results = player_repository.select_all()
team_results = team_repository.select_all()
game_results = game_repository.select_all()


# for player in player_results:
#     print(player.__dict__)

# for team in team_results:
#     print(team.__dict__)

for game in game_results:
    print(game.__dict__)

pdb.set_trace()