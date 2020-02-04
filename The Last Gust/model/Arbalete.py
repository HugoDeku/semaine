import pygame
from Entite.py import Entite

class Arbalete(Entite):

    def __init(self):
        super().__init__()
        self.vie = 4
        self.degat = 2
        self.velocity = 1
        self.tous_les_projectiles = pygame.sprite.Group()

        self.listes_sprites = {
            "haut": pygame.image.load('../assets/player.png'),
            "mouvement_haut": pygame.image.load('../assets/player.png'),
            "bas": pygame.image.load('../assets/player.png'),
            "mouvement_bas": pygame.image.load('../assets/player.png'),
            "droite": pygame.image.load('../assets/player.png'),
            "mouvement_droite": pygame.image.load('../assets/player.png'),
            "gauche": pygame.image.load('../assets/player.png'),
            "mouvement_gauche": pygame.image.load('../assets/player.png')

        }
        self.image_actu = self.listes_sprites["haut"]



    def lance_projectile(self):
        self.tous_les_projectiles.add(Projectile())