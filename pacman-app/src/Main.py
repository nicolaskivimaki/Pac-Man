from features.peli import Game
import pygame 

def main():
    """starts game
    """
    pygame.init()
    game = Game()
    game._run_game()
if __name__ == "__main__":
    main()
 