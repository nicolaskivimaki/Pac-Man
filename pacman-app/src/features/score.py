import pygame 

class Score:
    """ keeps the score
    """

    def __init__(self):
        self._money = 0
        self._lives = 3
        self._biggest_win = 0

    def _texts(self, screen):
        font = pygame.font.SysFont("arial black", 30)
        score_text = font.render(f'MONEY: ${self._money}', True, (20, 190, 20))
        lives_text = font.render(f'LIVES: {self._lives}', True, (220, 20, 20))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (690, 10))

