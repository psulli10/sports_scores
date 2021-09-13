import unittest
from models.attribute import Attribute
from models.player import Player
from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.attributes_1 = Attribute(10, 10, 10, 10, 10)
        self.attributes_2 = Attribute(8, 8, 8, 8, 8)
        self.team_attributes = Attribute(0, 0, 0, 0, 0)
        self.team = Team("St Mirren", self.team_attributes)
        self.player_1 = Player("Peter Sullivan", self.attributes_1, 3, "Defender", self.team)
        self.player_2 = Player("Curtis Main", self.attributes_2, 9, "Attacker", self.team)

    def test_can_get_name(self):
        self.assertEqual("St Mirren", self.team.name)

    def test_players_list_starts_empty(self):
        print("players dict: ", self.team.players)
        self.assertEqual(0, self.team.get_total_players())

    def test_wins_start_empty(self):
        self.assertEqual(0, self.team.wins)

    def test_draws_start_empty(self):
        self.assertEqual(0, self.team.draws)

    def test_defeats_start_empty(self):
        self.assertEqual(0, self.team.defeats)

    def test_can_add_player(self):
        self.team.add_player(self.player_1)
        self.assertEqual(1, self.team.get_total_players())

    def test_can_remove_player(self):
        self.team.add_player(self.player_1)
        self.team.add_player(self.player_1)
        self.team.add_player(self.player_1)
        self.team.remove_player(self.player_1)
        self.assertEqual(2, self.team.get_total_players())

    def test_can_update_attributes(self):
        self.team.add_player(self.player_1)
        self.team.add_player(self.player_2)
        self.team.set_team_attributes()
        expected_attributes = Attribute(9, 9, 9, 9, 9)
        self.assertEqual(expected_attributes.__dict__, self.team.attributes.__dict__)

    def test_can_increase_results__win(self):
        self.team.update_result('wins')
        self.assertEqual(1, self.team.wins)

    def test_can_increase_results__draw(self):
        self.team.update_result('draws')
        self.assertEqual(1, self.team.draws)

    def test_can_increase_results__defeat(self):
        self.team.update_result('defeats')
        self.assertEqual(1, self.team.defeats)