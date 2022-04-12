import pygame

class Peli:

    def __init__(self):
        pygame.init()
        self.naytto = pygame.display.set_mode((1000, 1000))
        self.robo = pygame.image.load("/home/kivimani/ot-harjoitustyo/laskarit/pacman-app/src/assets/pacman.png")
        ## kuva netistä: https://www.freeiconspng.com/thumbs/pacman-png/pacman-png-18.png
        self.y = 50
        self.x = 50
        self.ylos = False
        self.alas = False
        self.oikealle = False
        self.vasemmalle = False
        self.kello = pygame.time.Clock()

    def _lataa_naytto(self):
        self.naytto.fill((0, 0, 0))
        self.naytto.blit(self.robo, (self.x, self.y))
        pygame.display.flip()
        self.kello.tick(60)
        

    def _handle_events(self):
        for tapahtuma in pygame.event.get():

            if tapahtuma.type == pygame.KEYDOWN:

                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = True
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = True
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = True

            if tapahtuma.type == pygame.KEYUP:

                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = False
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = False
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = False

            if tapahtuma.type == pygame.QUIT:
                exit()

    def _liikuta_vasen(self):
        
        if self.x > 0:
            self.x -= 10

    def _liikuta_oikea(self):

        if self.x < 1000-self.robo.get_width():
                self.x += 10

    def _liikuta_ylos(self):

        if self.y > 0:
                self.y -= 10

    def _liikuta_alas(self):

        if self.y < 1000-self.robo.get_height():
                self.y += 10



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

            
        

peli = Peli()

#while True:

#    peli._handle_events()
#    peli._liikuta()
#    peli._lataa_naytto()

       


    