import sys
import os
import pygame
from ominaisuudet.level import *
from ominaisuudet.events import Events
from ominaisuudet.pelipyorii import *
from sprites.pacman import Pacman
from sprites.ghosts import Ghosts
from ominaisuudet.score import Score

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
        self._score = Score()
        self._speed = 2
        self._level = Level(self._screen)
        self._events = Events()
        self._pacman = Pacman(self._speed)
        self._ghosts = []
        self._all_ghosts = pygame.sprite.Group()
        self._number_of_ghosts = 10
        self._event_handler = HandleEvents(self._events)

    def _run_game(self):

        if self._state == "playing":
            self._game_screen()      

    def _start_game(self):
        self._level._create_level()
        self._create_ghosts()
        self._screen.blit(self._pacman._pacman, (self._pacman.rect.x, self._pacman.rect.y))
        for ghost in self._ghosts:
            self._screen.blit(ghost._ghost, (ghost.rect.x, ghost.rect.y))
        pygame.display.update()
    
    def _create_ghosts(self):
        for i in range(self._number_of_ghosts):
            ghost = Ghosts(self._speed)
            self._ghosts.append(ghost)
            self._all_ghosts.add(ghost)

    def _money_collision(self):

        coin_collision = pygame.sprite.spritecollide(self._pacman, self._level._coins, True)
        for coin in coin_collision:
            self._score._money += 10
            self._level._coins.remove(coin)

        cash_collision = pygame.sprite.spritecollide(self._pacman, self._level._cash, True)
        for cash in cash_collision:
            self._score._money += 100
            self._level._cash.remove(cash)
    
    def _check_lives(self):
        direction = self._event_handler._handle_events()
        ghost_collision = self._pacman._collison_with_ghost(self._all_ghosts, self._ghosts, self._score, direction)
        if ghost_collision:
            self._score._lives -= 1
        if self._score._lives == 0:
            self._state = "over"


    def _game_render(self):
        self._level._draw_level()
        direction = self._event_handler._handle_events()
        self._pacman._can_move(direction, self._level._walls)
        self._check_lives()
        for ghost in self._ghosts:
            ghost._ghost_can_move(self._level._walls)
        for ghost in self._ghosts:
            self._screen.blit(ghost._ghost, (ghost.rect.x, ghost.rect.y))            
        self._money_collision()
        self._score._texts(self._screen)
        self._screen.blit(self._pacman._pacman, (self._pacman.rect.x, self._pacman.rect.y))
        

    def _game_screen(self):
        self._start_game()
        while True:
            self._event_handler._handle_events()
            self._game_render()
            pygame.display.update()
            self._clock.tick(60)
            

