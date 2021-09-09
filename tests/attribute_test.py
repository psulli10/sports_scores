import unittest
from models.attribute import Attribute

class TestAttribute(unittest.TestCase):

    def setUp(self):
        self.attribue = Attribute(1, 2, 3, 4, 5, 6)

    def test_can_get_strength(self):
        self.assertEqual(1, self.attribue.strength)
        
    def test_can_get_speed(self):
        self.assertEqual(2, self.attribue.speed)

    def test_can_get_intelligence(self):
        self.assertEqual(3, self.attribue.intelligence)

    def test_can_get_fitness(self):
        self.assertEqual(4, self.attribue.fitness)

    def test_can_get_adaptability(self):
        self.assertEqual(5, self.attribue.adaptability)

    def test_can_get_id(self):
        self.assertEqual(6, self.attribue.id)
