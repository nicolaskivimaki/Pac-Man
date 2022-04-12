import pygame

class Peli:

    def __init__(self):
        pygame.init()
        self.naytto = pygame.display.set_mode((1000, 1000))
        self.robo = pygame.image.load("/home/kivimani/ot-harjoitustyo/laskarit/pacman-app/src/assets/pacman.png")
        ## kuva netistä: https://www.freeiconspng.com/thumbs/pacman-png/pacman-png-18.png
        self.vihollinen = pygame.image.load("/home/kivimani/ot-harjoitustyo/laskarit/pacman-app/src/assets/pacman.png")
        self.y = 50
        self.x = 50
        self.vihollisen_x = 600
        self.vihollisen_y = 300
        self.ny = 2
        self.nx = 2
        self.ylos = False
        self.alas = False
        self.oikealle = False
        self.vasemmalle = False
        self.kello = pygame.time.Clock()

    def _lataa_naytto(self):
        self.naytto.fill((0, 0, 0))
        self.naytto.blit(self.robo, (self.x, self.y))
        self.naytto.blit(self.vihollinen, (self.vihollisen_x, self.vihollisen_y))
        pygame.display.flip()
        self.kello.tick(60)
        

    def _handle_events(self): 
        for tapahtuma in pygame.event.get():

            if tapahtuma.type == pygame.KEYDOWN: # pylint: disable=no-member

                if tapahtuma.key == pygame.K_LEFT:# pylint: disable=no-member
                    self.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:# pylint: disable=no-member
                    self.oikealle = True
                if tapahtuma.key == pygame.K_UP:# pylint: disable=no-member
                    self.ylos = True
                if tapahtuma.key == pygame.K_DOWN:# pylint: disable=no-member
                    self.alas = True

            if tapahtuma.type == pygame.KEYUP:# pylint: disable=no-member

                if tapahtuma.key == pygame.K_LEFT:# pylint: disable=no-member
                    self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:# pylint: disable=no-member
                    self.oikealle = False
                if tapahtuma.key == pygame.K_UP:# pylint: disable=no-member
                    self.ylos = False
                if tapahtuma.key == pygame.K_DOWN:# pylint: disable=no-member
                    self.alas = False

            if tapahtuma.type == pygame.QUIT:# pylint: disable=no-member
                exit()


    def _liikuta(self):
        if self.ylos:
            if self.y > 0:
                self.y -= 10
        if self.alas:
            if self.y < 1000-self.robo.get_height():
                self.y += 10
        if self.vasemmalle:
            if self.x > 0:
                self.x -= 10
        if self.oikealle:
            if self.x < 1000-self.robo.get_width():
                self.x += 10

    def _liikuta_vihollista(self):

        self.vihollisen_x += self.nx
        self.vihollisen_y += self.ny

        self.vihollisen_y += self.ny
        if self.ny > 0 and self.vihollisen_y+self.vihollinen.get_height() >= 1000:
            self.ny = -self.ny
        if self.ny < 0 and self.vihollisen_y <= 0:
            self.ny = -self.ny

        self.vihollisen_x += self.nx
        if self.nx > 0 and self.vihollisen_x+self.vihollinen.get_height() >= 1000:
            self.nx = -self.nx
        if self.nx < 0 and self.vihollisen_x <= 0:
            self.nx = -self.nx

            
        

peli = Peli()

while True:

    peli._handle_events()
    peli._liikuta()
    peli._liikuta_vihollista()
    peli._lataa_naytto()

       


    