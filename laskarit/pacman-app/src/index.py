import  pygame 
from pelipyorii import PeliPyorii
from peli import Peli
from events import Events

def main():
    alusta = pygame.display.set_mode((1000, 1000))
    peli = Peli(alusta)
    events = Events()
    peli_pyorii = PeliPyorii(peli, alusta, events)
    pygame.init()
    peli_pyorii.start()

if __name__ == "__main__":
    main()
