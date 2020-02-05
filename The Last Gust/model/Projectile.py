import pygame
from os import *

class Projectile(pygame.sprite.Sprite):

<<<<<<< HEAD
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
=======
    def __init__(self, joueur,  nom, degats, velocite):
        super().__init__()
        self.nom = nom
        self.image = pygame.image.load(path.join(path.dirname(__file__),"../assets/sprites/" + self.nom + ".png"))
        self.rect = self.image.get_rect()
        self.degats = degats
        self.velocite = velocite
        self.joueur = joueur
        self.direction = self.joueur.direction
        if self.direction =="bas":
            self.rect.y = self.joueur.rect.y + self.joueur.rect.height + 1
            self.rect.x = self.joueur.rect.x + self.joueur.rect.width/2 - self.rect.width/2
        elif self.direction =="haut":
            self.rect.y = self.joueur.rect.y - self.rect.height - 1
            self.rect.x = self.joueur.rect.x + self.joueur.rect.width/2 - self.rect.width/2
        elif self.direction =="gauche":
            self.rect.y = self.joueur.rect.y + self.joueur.rect.height/2 - self.rect.height/2
            self.rect.x = self.joueur.rect.x - self.rect.width - 1
        else:
            self.rect.y = self.joueur.rect.y + self.joueur.rect.height/2 - self.rect.height/2
            self.rect.x = self.joueur.rect.x + self.joueur.rect.width + 1

    def deplacement(self):
        if self.direction =="bas":
>>>>>>> b550e753c880728331cc2179534d43de6ff80715
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
        
    
