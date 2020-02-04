import pygame

class Entite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

    def estMort(self):
        if self.vie <= 0:
            return True

    def attaque(self):
        pass
