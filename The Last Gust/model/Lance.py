from Entite import *
import pygame

class Lance(Entite):

    def __init__(self, posx, posy):
        super().__init__("Lance")
        self.degats= 4

#         self.listes_sprites = {
#             "haut": pygame.image.load('../assets/player.png'),
#             "mouvement_haut": pygame.image.load('../assets/player.png'),
#             "bas": pygame.image.load('../assets/player.png'),
#             "mouvement_bas": pygame.image.load('../assets/player.png'),
#             "droite": pygame.image.load('../assets/player.png'),
#             "mouvement_droite": pygame.ima1/.png
# santosz@pc-dg-039-02:~/github/semaine/The Last Gust$
# ge.load('../assets/player.png'),
#             "gauche": pygame.image.load('../assets/player.png'),
#             "mouvement_gauche": pygame.image.load('../assets/player.png')
#
#         }

        # self.image_actu = self.listes_sprites["bas"]
        super().set_sprite(posx, posy)

    # def attaque(self,joueur):
    #     joueur.vie -= self.degats
    #
    # def deplacer_droite(self):
    #     self.image_actu = self.changement_sprite("mouvement_droite")
    #     self.rect.x += self.velocite
    #     self.image_actu = self.changement_sprite("droite")
    #
    # def deplacer_haut(self):
    #     self.image_actu = self.changement_sprite("mouvement_haut")
    #     self.rect.y -= self.velocite
    #     self.image_actu = self.changement_sprite("haut")
    #
    # def deplacer_bas(self):
    #     self.image_actu = self.changement_sprite("mouvement_bas")
    #     self.rect.y += self.velocite
    #     self.image_actu = self.changement_sprite("bas")
    #
    # def deplacer_gauche(self):
    #     self.image_actu = self.changement_sprite("mouvement_gauche")
    #     self.rect.x -= self.velocite
    #     self.image_actu = self.changement_sprite("gauche")
    #
    # def changement_sprite(self, nom):
    #     x = self.rect.x
    #     y = self.rect.y
    #     self.image_actu = self.listes_sprites[nom]
    #     self.rect = self.image_actu.get_rect()
    #     self.rect.x = x
    #     self.rect.y = y
