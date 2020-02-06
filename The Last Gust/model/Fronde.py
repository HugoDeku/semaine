from Entite import *
import pygame

class Fronde(Entite):

    def __init__(self, posx, posy):
        super().__init__("Fronde")
        self.vie = 4
        self.degats = 2
        self.tous_les_projectiles = pygame.sprite.Group()
        super().set_sprite(posx, posy)

    def lance_projectile(self):
        self.tous_les_projectiles.add(Projectile("caillou",self.degats,5,self.direction,self.rect.x,self.rect.y))

    def deplacer_droite(self):
        self.image_actu = self.changement_sprite("mouvement_droite")
        self.rect.x += self.velocite
        self.image_actu = self.changement_sprite("droite")

    def deplacer_haut(self):
        self.image_actu = self.changement_sprite("mouvement_haut")
        self.rect.y -= self.velocite
        self.image_actu = self.changement_sprite("haut")

    def deplacer_bas(self):
        self.image_actu = self.changement_sprite("mouvement_bas")
        self.rect.y += self.velocite
        self.image_actu = self.changement_sprite("bas")

    def deplacer_gauche(self):
        self.image_actu = self.changement_sprite("mouvement_gauche")
        self.rect.x -= self.velocite
        self.image_actu = self.changement_sprite("gauche")

    def changement_sprite(self, nom):
        x = self.rect.x
        y = self.rect.y
        self.image_actu = self.listes_sprites[nom]
        self.rect = self.image_actu.get_rect()
        self.rect.x = x
        self.rect.y = y
