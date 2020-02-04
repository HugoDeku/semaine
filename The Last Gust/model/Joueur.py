from Entite import *

class Joueur(Entite):

    def __init__(self, posx, posy):
        super().__init__("Billy")
        self.vie=12
        self.velocite=12
        self.image_actu=self.listes_sprites
        
        super().set_sprite(posx,posy)

    def subirDegats(self, degats):
        self.vie -= degats
    
