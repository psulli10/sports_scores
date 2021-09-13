import pdb
from models.attribute import Attribute
from models.player import Player
from models.team import Team
import repositories.player_repository as player_repository
import repositories.team_repository as team_repository

player_repository.delete_all()
team_repository.delete_all()

player_attributes_1 = Attribute(10, 10, 10, 10, 10)
team_1 = Team("St Mirren")
team_repository.save(team_1)
player_1 = Player("Jamie McGrath", player_attributes_1, 7, "Midfielder", team_1)
player_repository.save(player_1)

player_1.squad_number = 10
player_repository.update(player_1)

player_results = player_repository.select_all()
team_results = team_repository.select_all()

for player in player_results:
    print(player.__dict__)

for team in team_results:
    print(team.__dict__)

pdb.set_trace()