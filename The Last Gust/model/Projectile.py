import pygame
import os
class Projectile(pygame.sprite.Sprite):

    def __init__(self, joueur,  nom, degats, velocite):
        super().__init__()
        self.nom = nom
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__),"../assets/sprites/" + self.nom + ".png"))
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
            self.rect.y += self.velocite
        elif self.direction =="haut":
            self.rect.y -= self.velocite
        elif self.direction =="gauche":
            self.rect.x -= self.velocite
        else:
            self.rect.x += self.velocite

    def infligedegats(self, entite):
        entite.subirDegats(self.degats)
        os.supprimer()
        
    
