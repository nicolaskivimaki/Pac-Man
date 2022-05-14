import sys
import os
import pygame
from ominaisuudet.level import *
from ominaisuudet.events import Events
from ominaisuudet.pelipyorii import *
from sprites.pacman import Pacman

dirname = os.path.dirname(__file__)

class Game:
    """ Luokka, joka luo, ylläpitää ja muokkaa pelin hahmoja"""

    def __init__(self):
        """Luokan konstruktori, joka luo pelin hahmot, antaa niille sijainnin ja säilyttää tietoja hahmon liikuttamisesta"""
        pygame.init()
        self._state = "playing"
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((840, 930))
        pygame.display.set_caption("Pacman")
        self._speed = 5
        self._level = Level(self._screen)
        self._events = Events()
        self._pacman = Pacman(self._speed)
        self._event_handler = HandleEvents(self._events)

    def _run_game(self):

        if self._state == "playing":
            self._game_screen()      

    def _start_game(self):
        self._level._create_level()
        self._screen.blit(self._pacman._pacman, (self._pacman.rect.x, self._pacman.rect.y))
        pygame.display.update()

    def _move_pacman(self, direction, opposite=None):
        if opposite:
            if direction == 1:
                self._pacman.rect.x += self._speed
            if direction == 2:
                self._pacman.rect.x -= self._speed
            if direction == 3:
                self._pacman.rect.y += self._speed
            if direction == 4:
                self._pacman.rect.y -= self._speed
        else:
            if direction == 1:
                self._pacman.rect.x -= self._speed
            if direction == 2:
                self._pacman.rect.x += self._speed
            if direction == 3:
                self._pacman.rect.y -= self._speed
            if direction == 4:
                self._pacman.rect.y += self._speed

    def _pacman_can_move(self):

        direction = self._event_handler._handle_events()
        self._move_pacman(direction)
        collision_test = pygame.sprite.spritecollide(self._pacman, self._level._walls, False)
        if collision_test:
            print("osui")
            self._move_pacman(direction, opposite=True)
            self._move_pacman(self._pacman._direction)
            collision_test = pygame.sprite.spritecollide(self._pacman, self._level._walls, False)
            if collision_test:
                print("osui")
                self._move_pacman(self._pacman._direction, opposite=True)
                self._pacman._direction = 0
            return
        self._pacman._direction = direction
        

    def _game_render(self):
        self._level._draw_level()
        self._pacman_can_move()
        self._screen.blit(self._pacman._pacman, (self._pacman.rect.x, self._pacman.rect.y))

    def _game_screen(self):
        self._start_game()
        while True:
            self._event_handler._handle_events()
            self._game_render()
            pygame.display.update()
            self._clock.tick(60)
            

