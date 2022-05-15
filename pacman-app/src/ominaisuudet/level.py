
import pygame
import sys
import os

dirname = os.path.dirname(__file__)


LEVEL_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 1],
        [1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
        [1, 2, 1, 2, 2, 0, 2, 0, 2, 0, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 0, 1],
        [1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1],
        [1, 2, 1, 0, 2, 2, 1, 2, 1, 2, 2, 0, 1, 2, 1, 1, 1, 2, 1, 2, 3, 2, 1, 2, 1, 1, 2, 1],
        [1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1],
        [1, 0, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 0, 2, 2, 2, 0, 1, 2, 1, 2, 1, 0, 2, 2, 0, 1],
        [1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1],
        [1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1],
        [1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 0, 1],
        [1, 2, 1, 2, 2, 2, 2, 0, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
        [1, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1],
        [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1],
        [1, 2, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1, 0, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 1],
        [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1],
        [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1],
        [1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 3, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]


class Level:

    def __init__(self, screen):
        self._screen = screen
        self._walls = pygame.sprite.Group()
        self._paths = pygame.sprite.Group()
        self._coins = pygame.sprite.Group()
        self._cash = pygame.sprite.Group()
        self._all_sprites = pygame.sprite.Group()

    def _create_level(self):
        block_size = 30
        level = LEVEL_1
        width, height = len(level[0]), len(level)
        for x in range(width):
            for y in range(height):
                block = level[y][x]
                coordinate_x = x * block_size
                coordinate_y = y * block_size
                self._place_blocks(block, coordinate_x, coordinate_y)
        
        self._place_blocks(block, coordinate_x, coordinate_y)
        
        self._group_sprites()

    def _group_sprites(self):

        self._all_sprites.add(self._paths, self._walls, self._coins, self._cash)

    def _place_blocks(self, block, x, y):

        if block == 1:
            self._walls.add(Wall(x, y))
        else:
            if block == 0:
                self._paths.add(Path(x, y))
            if block == 2:
                self._paths.add(Path(x, y))
                self._coins.add(Coin(x, y))
            if block == 3:
                self._paths.add(Path(x, y))
                self._cash.add(Cash(x, y))

    def _draw_level(self):
        self._all_sprites.draw(self._screen)


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((30, 30))
        self.image = image
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Path(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        image = pygame.Surface((30, 30))
        self.image = image
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load(os.path.join(dirname, "..", "assets", "coin.png"))
        self.image = pygame.transform.smoothscale(image, (12, 12))
        x += 9
        y += 9
        self.rect = pygame.Rect((x, y), (2, 2))


class Cash(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load(os.path.join(dirname, "..", "assets", "cash.png"))
        self.image = pygame.transform.smoothscale(image, (23, 23))
        x += 3
        y += 3
        self.rect = pygame.Rect((x, y), (5, 5))



