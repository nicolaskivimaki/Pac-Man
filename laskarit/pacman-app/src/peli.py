import pygame

class Peli:

    def __init__(self, alusta):
        pygame.init()
        self.naytto = alusta
        self.robo = pygame.image.load("/home/kivimani/ot-harjoitustyo/laskarit/pacman-app/src/assets/pacman.png")
        # kuva netistä: https://www.freeiconspng.com/thumbs/pacman-png/pacman-png-18.png
        self.vihollinen = pygame.image.load("/home/kivimani/ot-harjoitustyo/laskarit/pacman-app/src/assets/goblin.jpeg")
        # Tilapäinen kuva netistä: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pikpng.com%2Fpngvi%2FiibowJ_goblins-shop-is-a-pixel-art-simulation-game-in-which-pixel-goblin%2F&psig=AOvVaw2DuW_pqXEATlgOSg9EPMfm&ust=1649881569725000&source=images&cd=vfe&ved=0CAcQjRxqFwoTCKCn9_itj_cCFQAAAAAdAAAAABAb
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

    def paivita(self):

        self._liikuta()
        self._liikuta_vihollista()
        self._lataa_naytto()

    def _lataa_naytto(self):
        self.naytto.fill((0, 0, 0))
        self.naytto.blit(self.robo, (self.x, self.y))
        self.naytto.blit(self.vihollinen, (self.vihollisen_x, self.vihollisen_y))
        pygame.display.flip()
        self.kello.tick(60)


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

            
        

#peli = Peli()

#while True:

#    peli._handle_events()
#    peli._liikuta()
#    peli._liikuta_vihollista()
#    peli._lataa_naytto()

       


    