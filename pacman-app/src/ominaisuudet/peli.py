import sys
import os
import pygame
from ominaisuudet.events import Events
from ominaisuudet.pelipyorii import PeliPyorii
dirname = os.path.dirname(__file__)

class Peli:
    """ Luokka, joka luo, ylläpitää ja muokkaa pelin hahmoja"""

    def __init__(self):
        """Luokan konstruktori, joka luo pelin hahmot, antaa niille sijainnin ja säilyttää tietoja hahmon liikuttamisesta"""

        pygame.init()
        self.tila = "start"
        self.kaynnissa = True
        self.korkeus = 1000
        self.leveys = 1000
        self.naytto = pygame.display.set_mode((self.korkeus, self.leveys))
        self.kello = pygame.time.Clock()
        self.robo = pygame.image.load(os.path.join(dirname, "..", "assets", "pacman.png"))
        self.robo = pygame.transform.smoothscale(self.robo, (50, 50))
        self.vihollinen = pygame.image.load(os.path.join(dirname, "..", "assets", "goblin.jpeg"))
        self.vihollinen = pygame.transform.smoothscale(self.vihollinen, (50, 50))
        self.y = 50 # pylint: disable=invalid-name
        self.x = 50 # pylint: disable=invalid-name
        self.vihollisen_x = 600 # pylint: disable=invalid-name
        self.vihollisen_y = 300 # pylint: disable=invalid-name
        self.ny = 2 # pylint: disable=invalid-name
        self.nx = 2 # pylint: disable=invalid-name
        self.ylos = False
        self.alas = False
        self.oikealle = False
        self.vasemmalle = False

    def _tekstit(self, words, screen, pos, size, colour, font_name, centered=False):
        """Luo tekstin ulkonäköä"""

        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def _aloita_tapahtumat(self):
        """Asetetaan pelin tila"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.kaynnissa = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.tila = 'pelaa'

    def start_draw(self):
        """Piirretään tekstit näytölle"""

        self.naytto.fill((0, 0, 0))
        self._tekstit('PAINA "a" ALOITTAAKSESI', self.naytto, [self.leveys//2, self.korkeus//2], 50, (100, 200, 100), 'arial light', centered=True)
        self._tekstit('TERVETULOA!', self.naytto, [self.leveys//2, self.korkeus//2-80], 50, (250, 0, 0), 'arial black', centered=True)
        self._tekstit('ENKKA:', self.naytto, [self.leveys//2, 15], 24, (255, 255, 255), 'arial black', centered=True)
        pygame.display.update()

    def paivita(self):
        """Päivittää """
        self._liikuta()
        self._liikuta_vihollista()
        self._lataa_naytto()

    def _lataa_naytto(self):
        self.naytto.fill((0, 0, 0))
        self.naytto.blit(self.robo, (self.x, self.y))
        self.naytto.blit(self.vihollinen, (self.vihollisen_x, self.vihollisen_y))
        pygame.display.flip()
        self.kello.tick(60)

    def _liikuta(self):
        if self.ylos:
            if self.y > 0:
                self.y -= 10
        if self.alas:
            if self.y < self.korkeus-self.robo.get_height():
                self.y += 10
        if self.vasemmalle:
            if self.x > 0:
                self.x -= 10
        if self.oikealle:
            if self.x < self.leveys-self.robo.get_width():
                self.x += 10

    def _liikuta_vihollista(self):
        self.vihollisen_x += self.nx
        self.vihollisen_y += self.ny
        self.vihollisen_y += self.ny
        if self.ny > 0 and self.vihollisen_y+self.vihollinen.get_height() >= self.korkeus:
            self.ny = -self.ny
        if self.ny < 0 and self.vihollisen_y <= 0:
            self.ny = -self.ny
        self.vihollisen_x += self.nx
        if self.nx > 0 and self.vihollisen_x+self.vihollinen.get_height() >= self.leveys:
            self.nx = -self.nx
        if self.nx < 0 and self.vihollisen_x <= 0:
            self.nx = -self.nx

    def _kaynnista(self):
        while self.kaynnissa:
            if self.tila == 'start':
                self._aloita_tapahtumat()
                self.start_draw()
            elif self.tila == "pelaa":
                self._aloita_peli()
            else:
                self.kaynnissa = False
            self.kello.tick(60)
        pygame.quit()
        sys.exit()

    def _aloita_peli(self):
        events = Events()
        peli = Peli()
        peli_pyorii = PeliPyorii(peli, self.naytto, events)
        pygame.init()
        peli_pyorii.start()
