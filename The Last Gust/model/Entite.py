import pygame

class Entite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.nom = "default"
        self.vie = 1
        self.velocite = 1
        self.path = "../assets/sprite/" + self.nom
        self.listes_sprites = {
            "haut": pygame.image.load(self.path + '_haut.png'),
            "mouvement_haut": pygame.image.load(self.path+'.png'),
            "bas": pygame.transform.rotate(self.listes_sprites["haut"], 180),
            "mouvement_bas": pygame.transform.rotate(self.listes_sprites["mouvement_haut"], 180),
            "droite": pygame.transform.rotate(self.listes_sprites["bas"], 270),
            "mouvement_droite": pygame.transform.rotate(self.listes_sprites["mouvement_haut"], 270),
            "gauche": pygame.transform.rotate(self.listes_sprites["bas"], 90),
            "mouvement_gauche": pygame.transform.rotate(self.listes_sprites["mouvement_haut"], 90),
        }
    def estMort(self):
        if self.vie <= 0:
            return True

    def attaque(self):
        pass
