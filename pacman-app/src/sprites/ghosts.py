import pygame
import os
from random import randint
dirname = os.path.dirname(__file__)

class Ghosts(pygame.sprite.Sprite):

    def __init__(self, speed):
        super().__init__()
        self._ghost = pygame.image.load(os.path.join(dirname, "..", "assets", "ghost.png"))
        self._ghost = pygame.transform.smoothscale(self._ghost, (30, 30))
        self._speed = speed
        self.rect = self._ghost.get_rect()
        self.rect.x = 600
        self.rect.y = 600
        self._direction = 3
        self._counter = 30
        
    def _move_ghost(self, direction, opposite=False):
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

    def _choose_direction(self, walls):
        direction = self._ghost_can_turn(walls)
        number = randint(0,1)
        if self._direction == 0:
            return direction
        elif number == 0:
            return direction
        return self._direction
        #self._counter -= 1
        #return self._direction

    def _ghost_can_move(self, walls):
        if self.rect.y < 60:
            self.rect.y = 930
            self.rect.x = 390
        if self.rect.y > 930:
            self.rect.y = 60
            self.rect.x = 390
        direction = self._choose_direction(walls)
        self._move_ghost(direction)
        collision_test = pygame.sprite.spritecollide(self, walls, False)
        if collision_test:
            self._move_ghost(direction, opposite=True)
            self._move_ghost(self._direction)
            collision_test = pygame.sprite.spritecollide(self, walls, False)
            if collision_test:
                self._move_ghost(self._direction, opposite=True)
                self._direction = 0
            return
        self._direction = direction
        

    def _ghost_can_turn(self, walls):
        turns = self._turns(self._direction)
        for direction in turns:
            self._move_ghost(direction)
            collision_test = pygame.sprite.spritecollide(self, walls, False)
            if not collision_test:
                self._move_ghost(direction, opposite=True)
                return direction
            self._move_ghost(direction, opposite=True)
        return self._direction
            
    def _turns(self, direction):
        number = randint(0,1)
        if direction == 1:
            turns = [[3, 4], [4, 3]]
            return turns[number]
        elif direction == 2:
            turns = [[3, 4], [4, 3]]
            return turns[number]
        elif direction == 4:
            turns = [[1, 2], [2, 1]]
            return turns[number]
        elif direction == 3:
            turns = [[1, 2], [2, 1]]
            return turns[number]
        elif direction == 0:
            return [randint(1, 4), randint(1, 4)]


                

