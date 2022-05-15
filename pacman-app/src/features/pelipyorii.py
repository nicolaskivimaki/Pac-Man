import sys
import pygame
from sprites.pacman import Pacman

class Events:
    def get(self):
        return pygame.event.get()

class HandleEvents:
    def __init__(self, events):
        self._events = events
        self._quit = False
        self._direction = 0
        
    def _handle_events(self):
        """Set direction of pacman.
            Left = 1
            Right = 2
            Up = 3
            Down = 4
        """
        for tapahtuma in self._events.get():
            if tapahtuma.type == pygame.KEYDOWN: # pylint: disable=no-member
                if tapahtuma.key == pygame.K_LEFT:# pylint: disable=no-member
                    self._direction = 1

                if tapahtuma.key == pygame.K_RIGHT:# pylint: disable=no-member
                    self._direction = 2

                if tapahtuma.key == pygame.K_UP:# pylint: disable=no-member
                    self._direction = 3

                if tapahtuma.key == pygame.K_DOWN:# pylint: disable=no-member
                    self._direction = 4

            if tapahtuma.type == pygame.QUIT:# pylint: disable=no-member
                self._quit = True
                sys.exit()
        
        return self._direction
