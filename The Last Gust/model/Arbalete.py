import pygame
from Entite import *
from Projectile import *

class Arbalete(Entite):

    def __init__(self, posx, posy):
        super().__init__()
        self.vie = 4
        self.degat = 2
        self.velocite = 1
        self.tous_les_projectiles = pygame.sprite.Group()

        self.listes_sprites = {
            "haut": pygame.image.load('../assets/player.png'),
            "mouvement_haut": pygame.image.load('../assets/player.png'),
            "bas": pygame.image.load('../assets/player.png'),
            "mouvement_bas": pygame.image.load('../assets/player.png'),
            "droite": pygame.image.load('../assets/player.png'),
            "mouvement_droite": pygame.image.load('../assets/player.png'),
            "gauche": pygame.image.load('../assets/player.png'),
            "mouvement_gauche": pygame.image.load('../assets/player.png'),
            "animation_attaque": pygame.image_load('../assets/player.png')

        }

        self.image_actu = self.listes_sprites["bas"]
        self.rect = self.image_actu.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.direction ="bas"

    def lance_projectile(self):
        self.tous_les_projectiles.add(Projectile("fleche",self.degats,5,self.direction,self.rect.x,self.rect.y)


    def deplacer_droite(self):
        self.image_actu = self.changement_sprite("mouvement_droite")
        self.rect.x += self.velocite
        self.image_actu = self.changement_sprite("droite")
        self.direction = "droite"

    def deplacer_haut(self):
        self.image_actu = self.changement_sprite("mouvement_haut")
        self.rect.y -= self.velocite
        self.image_actu = self.changement_sprite("haut")
        self.direction = "haut"

    def deplacer_bas(self):
        self.image_actu = self.changement_sprite("mouvement_bas")
        self.rect.y += self.velocite
        self.image_actu = self.changement_sprite("bas")
        self.direction = "bas"

    def deplacer_gauche(self):
        self.image_actu = self.changement_sprite("mouvement_gauche")
        self.rect.x -= self.velocite
        self.image_actu = self.changement_sprite("gauche")
        self.direction = "gauche"

    def changement_sprite(self, nom):
        x = self.rect.x
        y = self.rect.y
        self.image_actu = self.listes_sprites[nom]
        self.rect = self.image_actu.get_rect()
        self.rect.x = x
        self.rect.y = y