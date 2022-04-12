import unittest

from peli import Peli

class TestPeli(unittest.TestCase):

    def setUp(self):
        self.peli = Peli()

    def test_toimiiko_vasen_reuna(self):
        self.peli.ylos = True
        for i in range(10):
            self.peli._liikuta()
        self.assertEqual(str(self.peli.y), "0")

