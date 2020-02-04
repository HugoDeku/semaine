import pygame

class Entite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.vie = 1
        self.velocite = 1
        self.sprites = {}
    def estMort(self):
        if self.vie <= 0:
            return True

    def attaque(self):
        pass
    def deplacement_haut():
