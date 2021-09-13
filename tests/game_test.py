import unittest
from models.attribute import Attribute
from models.player import Player
from models.team import Team
from models.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.attributes_1 = Attribute(10, 10, 10, 10, 10)
        self.attributes_2 = Attribute(8, 8, 8, 8, 8)
        self.team_attributes = Attribute(8, 8, 8, 8, 8)
        self.team_1 = Team("St Mirren", self.team_attributes)
        self.team_1.id = 1
        self.team_2 = Team("Greenock Morton", self.team_attributes)
        self.team_2.id = 2
        self.player_1 = Player("Peter Sullivan", self.attributes_1, 3, "Defender",  self.team_1)
        self.player_2 = Player("Curtis Main", self.attributes_2, 9, "Attacker", self.team_1)
        self.game = Game(self.team_1, self.team_2, 4, 0)

    def test_can_get_home_team(self):
        self.assertEqual(self.team_1, self.game.home)

    def test_can_get_away_team(self):
        self.assertEqual(self.team_2, self.game.away)

    def test_can_get_home_team_goals(self):
        self.assertEqual(4, self.game.home_goals)

    def test_can_get_away_team_goals(self):
        self.assertEqual(0, self.game.away_goals)

    # def test_result_starts_not_determined(self):
    #     self.assertEqual("To be determined...", self.game.result)

    def test_can_get_result__home_win(self):
        self.assertEqual(1, self.game.get_result())

    def test_can_get_result__away_win(self):
        game_away_win = Game(self.team_1, self.team_2, 1, 2)
        # print("away game dictionary", game_away_win.__dict__)
        self.assertEqual(2, game_away_win.get_result())

    def test_can_get_result__draw(self):
        game_draw = Game(self.team_1, self.team_2, 1, 1)
        self.assertEqual(0, game_draw.get_result())