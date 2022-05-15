import pygame
import os

dirname = os.path.dirname(__file__)

class Pacman(pygame.sprite.Sprite):

    def __init__(self, speed, image=None):
        self._pacman = pygame.image.load(os.path.join(dirname, "..", "assets", "pacman.png"))
        self._pacman = pygame.transform.smoothscale(self._pacman, (30, 30))
        self._speed = speed
        self.rect = self._pacman.get_rect()
        self.rect.x = 210
        self.rect.y = 300
        self._direction = 0









