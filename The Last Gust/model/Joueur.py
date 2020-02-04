import pygame
from Entite import *
from Projectile import *

class Joueur(Entite):

    def __init__(self, posx, posy):
        super().__init__("Billy")
        self.vie=12
        self.velocite=12
        self.image_actu=self.listes_sprites
        self.touches = {}
        super().set_sprite(posx,posy)

    def lance_projectile(self):
        self.projectiles.add(Projectile("Tornade",0,21,self.direction,self.rect.x,self.rect.y))
        
    
