import pygame
from os import *
import path
from Jeu import *

running = True
root = path.dirname(__file__)
background = pygame.image.load(path.join(root, "assets/sprites/bg_temp.png"))

#chargement du jeu
jeu = Jeu()

pygame.display.set_caption("The Last Gust")
ecran = pygame.display.set_mode((1024,768))


#boucle jeu

while running:
    #appliquer background
    ecran.blit(background, (0, 0))

    #appliquer le joueur
    ecran.blit(jeu.joueur.image_actu, jeu.joueur.rect)


    if jeu.pressed.get(pygame.K_RIGHT):
        jeu.joueur.deplacer_droite()
    elif jeu.pressed.get(pygame.K_LEFT):
        jeu.joueur.deplacer_gauche()
    elif jeu.pressed.get(pygame.K_UP):
        jeu.joueur.deplacer_haut()
    elif jeu.pressed.get(pygame.K_DOWN):
        jeu.joueur.deplacer_bas()

    if not jeu.pressed.get(pygame.K_RIGHT) and not jeu.pressed.get(pygame.K_LEFT) and not jeu.pressed.get(pygame.K_UP) and not jeu.pressed.get(pygame.K_DOWN) :
        jeu.joueur.arret_deplacement()

    #maj ecran
    pygame.display.flip()

    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        #event = close window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #detecter lorque qu'un joueur presse une touche
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                jeu.joueur.launch_projectile()
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False
