import pygame
class Peli:
    def __init__(self, alusta):
        pygame.init()
        self.naytto = alusta
        self.robo = pygame.image.load("/home/kivimani/ot-harjoitustyo/laskarit/pacman-app/src/assets/pacman.png")
        self.vihollinen = pygame.image.load("/home/kivimani/ot-harjoitustyo/laskarit/pacman-app/src/assets/goblin.jpeg")
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
        self.kello = pygame.time.Clock()

    def paivita(self):
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
            if self.y < 1000-self.robo.get_height():
                self.y += 10
        if self.vasemmalle:
            if self.x > 0:
                self.x -= 10
        if self.oikealle:
            if self.x < 1000-self.robo.get_width():
                self.x += 10

    def _liikuta_vihollista(self):
        self.vihollisen_x += self.nx
        self.vihollisen_y += self.ny
        self.vihollisen_y += self.ny
        if self.ny > 0 and self.vihollisen_y+self.vihollinen.get_height() >= 1000:
            self.ny = -self.ny
        if self.ny < 0 and self.vihollisen_y <= 0:
            self.ny = -self.ny
        self.vihollisen_x += self.nx
        if self.nx > 0 and self.vihollisen_x+self.vihollinen.get_height() >= 1000:
            self.nx = -self.nx
        if self.nx < 0 and self.vihollisen_x <= 0:
            self.nx = -self.nx
    