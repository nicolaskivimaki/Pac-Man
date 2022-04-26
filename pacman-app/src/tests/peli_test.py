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

    def test_toimiiko_oikea_reuna(self):
        self.peli.oikealle = True
        for i in range(1000):
            self.peli._liikuta()
        leveys = self.peli.robo.get_width()
        self.assertEqual(str(self.peli.x), f"{self.peli.leveys-leveys}")

    def test_toimiiko_ylareuna(self):
        self.peli.ylos = True
        for i in range(1000):
            self.peli._liikuta()
        korkeus = self.peli.robo.get_height()
        self.assertEqual(str(self.peli.y), "0")

    def test_toimiiko_alareuna(self):
        self.peli.alas = True
        for i in range(1000):
            self.peli._liikuta()
        korkeus = self.peli.robo.get_height()
        self.assertEqual(str(self.peli.y), f"{self.peli.korkeus-korkeus}")

    def test_liikkuuko_toinen_hahmo_ylos(self):
        for i in range(10):
            self.peli._liikuta_vihollista()
        self.assertNotEqual(str(self.peli.vihollisen_y), "300")

    def test_liikkuuko_toinen_hahmo_sivulle(self):
        for i in range(10):
            self.peli._liikuta_vihollista()
        self.assertNotEqual(str(self.peli.vihollisen_x), "600")

    def test_toimiiko_tilan_asettaminen(self):
        self.assertEqual(str(self.peli.tila), "start")

    def test_liikkuuko_pacman_alas(self):
        self.peli.y = 50
        self.peli.alas = True
        self.peli._liikuta()
        leveys = self.peli.robo.get_width()
        self.assertGreater((self.peli.y), 50)

    def test_liikkuuko_pacman_ylos(self):
        self.peli.y = 100
        self.peli.ylos = True
        self.peli._liikuta()
        leveys = self.peli.robo.get_width()
        self.assertLess((self.peli.y), 100)

    def test_liikkuuko_pacman_oikealle(self):
        self.peli.x = 100
        self.peli.oikealle = True
        self.peli._liikuta()
        leveys = self.peli.robo.get_width()
        self.assertGreater((self.peli.x), 100)

    def test_liikkuuko_pacman_vasemmalle(self):
        self.peli.x = 100
        self.peli.vasemmalle = True
        self.peli._liikuta()
        leveys = self.peli.robo.get_width()
        self.assertLess((self.peli.x), 100)
