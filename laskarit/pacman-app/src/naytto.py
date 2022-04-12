import pygame 

class Naytto:
    def __init__(self, alusta, peli):
        self._alusta = alusta
        self._peli = peli

    def tayta(self):
        self._alusta.fill((0, 0, 0))
        self._alusta.blit(self._peli.robo, (self._peli.x, self._peli.y))
        self._alusta.blit(self._peli.vihollinen, (self._peli.vihollisen_x, self._peli.vihollisen_y))
        pygame.display.flip()