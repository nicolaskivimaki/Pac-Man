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
    
    def _move_pacman(self, direction, opposite=None):
        if opposite:
            if direction == 1:
                self.rect.x += self._speed
            if direction == 2:
                self.rect.x -= self._speed
            if direction == 3:
                self.rect.y += self._speed
            if direction == 4:
                self.rect.y -= self._speed
        else:
            if direction == 1:
                self.rect.x -= self._speed
            if direction == 2:
                self.rect.x += self._speed
            if direction == 3:
                self.rect.y -= self._speed
            if direction == 4:
                self.rect.y += self._speed

    def _can_move(self, direction, walls):
        self._move_pacman(direction)
        collision_test = pygame.sprite.spritecollide(self, walls, False)
        if collision_test:
            self._move_pacman(direction, opposite=True)
            self._move_pacman(self._direction)
            collision_test = pygame.sprite.spritecollide(self, walls, False)
            if collision_test:
                self._move_pacman(self._direction, opposite=True)
                self._direction = 0
            return
        self._direction = direction
        if self.rect.y < 50:
            self.rect.y = 930
        if self.rect.y > 930:
            self.rect.y = 50

    def _collison_with_ghost(self, ghosts, ghostlist, score, direction):
        self._move_pacman(direction)
        collision = pygame.sprite.spritecollide(self, ghosts, True)
        if collision:
            self._move_pacman(direction, opposite=True)
            self._direction = 0
            for ghost in collision:
                ghosts.remove(ghost)
                ghostlist.remove(ghost)
            self._move_pacman(direction, opposite=True)
            return True
        self._move_pacman(direction, opposite=True)








