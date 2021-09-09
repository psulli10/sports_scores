import pdb
from models.attribute import Attribute
from models.player import Player
import repositories.player_repository as player_repository

player_repository.delete_all()

player_attributes_1 = Attribute(10, 10, 10, 10, 10)
player_1 = Player("Jamie McGrath", player_attributes_1, 7)
player_repository.save(player_1)

player_results = player_repository.select_all()

for player in player_results:
    print(player.__dict__)

pdb.set_trace()