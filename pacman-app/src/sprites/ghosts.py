import pygame
import os
dirname = os.path.dirname(__file__)

class Ghosts(pygame.sprite.Sprite):

    def __init__(self, speed):
        self._ghost = pygame.image.load(os.path.join(dirname, "..", "assets", "ghost.png"))
        self._pacman = pygame.transform.smoothscale(self._pacman, (30, 30))
        self._speed = speed
        self.rect = self._pacman.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        self._direction = 0
        