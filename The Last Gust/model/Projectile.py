from Entite import *
import pygame

    class Projectile(Entite.Entite):

        def __init(self,sprite, degats, velocite,direction ):
             super().__init__();
             self.degats = degats
             self.velocite = velocite
             self.direction = direction
             self.sprite = sprite
             self.rect = self.image_actu.get_rect()
             self.rect.x = posx
             self.rect.y = posy

        def deplacement(self):
            if self.direction = "bas":
               self.rect.y += self.velocite
            elif self.direction = "haut":
                self.rect.y -= self.velocite
            elif self.direction = "gauche":
                self.rect.x -= self.velocite
            else :
                self.rect.x += self.velocite

        def infligeDegats(self,joueur):
            joueur.vie -= self.degats
