import unittest
from models.player import Player
from models.attribute import Attribute

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.attributes = Attribute(10, 10, 10 , 10, 10)
        self.player = Player("Peter Sullivan", self.attributes, 3, 5)

    def test_can_get_name(self):
        self.assertEqual("Peter Sullivan", self.player.name)

    def test_can_get_squad_number(self):
        self.assertEqual(3, self.player.squad_number)

    def test_can_get_attributes(self):
        self.assertEqual(self.attributes, self.player.attributes)

    def test_can_get_id(self):
        self.assertEqual(5, self.player.id)