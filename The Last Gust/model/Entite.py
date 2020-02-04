import pygame
from os import *

class Entite(pygame.sprite.Sprite):

    #Constructeur de la class Entite
    def __init__(self, nom):
        self.root = path.dirname(__file__)
        super().__init__()
        self.nom = nom
        self.vie = 1
        self.velocite = 1
        self.path = "../assets/sprites/" + self.nom
        self.listes_sprites = {}
        self.image_actu = 0
        self.rect = 0
        self.direction ="bas"

    def estMort(self):
        if self.vie <= 0:
            return True

    def attaque(self):
        pass

    def set_sprite(self, posx, posy):
        self.listes_sprites = {
            "haut": pygame.image.load(path.join(self.root, self.path) + "_haut.png"),
            "mouvement_haut": pygame.image.load(path.join(self.root, self.path)+'_mouvHaut.png'),
        }
        self.listes_sprites.update({'bas': pygame.transform.rotate(self.listes_sprites["haut"], 180)})
        self.listes_sprites.update({'bas':pygame.transform.rotate(self.listes_sprites["haut"], 180)})
        self.listes_sprites.update({'mouvement_bas': pygame.transform.rotate(self.listes_sprites["mouvement_haut"], 180)})
        self.listes_sprites.update({'droite':  pygame.transform.rotate(self.listes_sprites["haut"], 270)})
        self.listes_sprites.update({'mouvement_droite':  pygame.transform.rotate(self.listes_sprites["mouvement_haut"], 270)})
        self.listes_sprites.update({'gauche': pygame.transform.rotate(self.listes_sprites["haut"], 90)})
        self.listes_sprites.update({'mouvement_gauche': pygame.transform.rotate(self.listes_sprites["mouvement_haut"], 90)})

        self.image_actu = self.listes_sprites["bas"]
        self.rect = self.image_actu.get_rect()
        self.rect.x = posx
        self.rect.y = posy


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

    def subirDegats(self, degats):
        self.vie -= degats

    def infligeDegat(self, entite)
