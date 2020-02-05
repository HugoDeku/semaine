import pygame
from Entite import *
from Projectile import *
from time import time

class Joueur(Entite):

    def __init__(self, posx, posy):
        super().__init__("Joueur")
        self.vie=12
        self.vie_max = 12
        self.velocite=14
        self.image_actu=self.listes_sprites
        self.projectiles = pygame.sprite.Group()
        super().set_sprite(posx,posy)



    def lance_projectile(self, effect):
        if 'tempsRecup' in self.__dict__:
            if time() - self.tempsRecup > 0.5:
                effect.play()
                self.projectiles.add(Projectile(self, "tornade",0, 20))
                self.tempsRecup = time()
        else:
            effect.play()
            self.projectiles.add(Projectile(self, "tornade", 0, 20))
            self.tempsRecup = time()
