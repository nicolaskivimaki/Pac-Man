from curses import KEY_A1, KEY_DOWN
import unittest
import pygame
from peli import Peli

class TestPeli(unittest.TestCase):

    def setUp(self):
        self.peli = Peli()

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
        self.assertEqual(str(self.peli.x), f"{self.peli.leveys-leveys}")

    def test_liikkuuko_toinen_hahmo_ylos(self):
        for i in range(10):
            self.peli._liikuta_vihollista()
        self.assertNotEqual(str(self.peli.vihollisen_y), "300")

    def test_liikkuuko_toinen_hahmo_sivulle(self):
        for i in range(10):
            self.peli._liikuta_vihollista()
        self.assertNotEqual(str(self.peli.vihollisen_x), "600")

    def test_toimiiko_alkunaytto(self):
        self.peli._kaynnista()
        event = pygame.event.Event(pygame.KEYDOWN, pygame.K_a)
        pygame.event.post(event)
        self.assertEqual(str(self.peli.tila), "pelaa")

    

