import unittest

from peli import Peli

class TestPeli(unittest.TestCase):

    def setUp(self):
        self.peli = Peli()

    def test_toimiiko_vasen_reuna(self):
        for i in range(10):
            self.peli._liikuta_vasen()

        self.assertEqual(str(self.peli.x), "0")

