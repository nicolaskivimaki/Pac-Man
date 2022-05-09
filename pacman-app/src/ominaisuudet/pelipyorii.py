import sys
import pygame

class PeliPyorii:
    def __init__(self, peli, alusta, events):
        self._peli = peli
        #self._naytto = naytto
        self._alusta = alusta
        self._events = events
    def start(self):
        while True:
            self._handle_events()
            self._peli.paivita()
            # self._naytto.tayta()
    def _handle_events(self):
        for tapahtuma in self._events.get():
            if tapahtuma.type == pygame.KEYDOWN: # pylint: disable=no-member
                if tapahtuma.key == pygame.K_LEFT:# pylint: disable=no-member
                    self._peli.vasemmalle = True
                    self._peli.oikealle = False
                    self._peli.ylos = False
                    self._peli.alas = False
                if tapahtuma.key == pygame.K_RIGHT:# pylint: disable=no-member
                    self._peli.vasemmalle = False
                    self._peli.oikealle = True
                    self._peli.ylos = False
                    self._peli.alas = False
                if tapahtuma.key == pygame.K_UP:# pylint: disable=no-member
                    self._peli.vasemmalle = False
                    self._peli.oikealle = False
                    self._peli.ylos = True
                    self._peli.alas = False
                if tapahtuma.key == pygame.K_DOWN:# pylint: disable=no-member
                    self._peli.vasemmalle = False
                    self._peli.oikealle = False
                    self._peli.ylos = False
                    self._peli.alas = True
            if tapahtuma.type == pygame.QUIT:# pylint: disable=no-member
                sys.exit()
