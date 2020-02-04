import pygame
from os import *

class Projectile(pygame.sprite.Sprite):

    def __init(self, nom, degats, velocite, direction, posx, posy, entite):
        self.root = path.dirname(__file__)
        super().__init__()
        self.entite=entite
        self.degats = degats
        self.velocite = velocite
        self.direction = direction
        self.nom = nom
        self.path = "../assets/sprites/" + self.nom
        self.listes_sprites = {}
        self.image_actu = 0
        self.rect = 0
        
        
    def set_sprite(self, posx, posy):
        self.listes_sprites = {
            "haut": pygame.image.load(path.join(self.root, self.path) + "_haut.png"),
            "mouvement_haut": pygame.image.load(path.join(self.root, self.path)+'_mouvHaut.png'),
        }
        self.listes_sprites.update({'mouvement_haut':pygame.transform.flip(self.listes_sprites["haut"],true,false)})
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
        
    def supprimer(self):
        self.entite.projectiles.remove(self)
        
    def deplacement(self):

        if self.rect.x<=0 or self.rect.x>=1024 or self.rect.y <=0 or self.rect.y>= 768:
            supprimer()
        
        elif self.direction =="bas":
            self.rect.y += self.velocite
        elif self.direction =="haut":
            self.rect.y -= self.velocite
        elif self.direction =="gauche":
            self.rect.x -= self.velocite
        else:
            self.rect.x += self.velocite

    def infligedegats(self, entite):
        entite.subirDegats(self.degats)
        supprimer()
        
    
