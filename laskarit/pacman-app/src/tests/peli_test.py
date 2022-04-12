import unittest
import pygame
from peli import Peli

class TestPeli(unittest.TestCase):

    def setUp(self):
        alusta = pygame.display.set_mode((1000, 1000))
        self.peli = Peli(alusta)

    def test_toimiiko_vasen_reuna(self):
        self.peli.ylos = True
        for i in range(10):
            self.peli._liikuta()
        self.assertEqual(str(self.peli.y), "0")

    def test_toimiiko_oikea_reuna(self):
        self.peli.oikealle = True
        for i in range(1000):
            self.peli._liikuta()
        leveys = self.peli.robo.get_width()
        self.assertEqual(str(self.peli.x), f"{1000-leveys}")

    def test_liikkuuko_toinen_hahmo_ylos(self):
        for i in range(10):
            self.peli._liikuta_vihollista()
        self.assertNotEqual(str(self.peli.vihollisen_y), "300")

    def test_liikkuuko_toinen_hahmo_sivulle(self):
        for i in range(10):
            self.peli._liikuta_vihollista()
        self.assertNotEqual(str(self.peli.vihollisen_x), "600")

    

