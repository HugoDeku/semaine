import pygame

from Salle import *

def setSalle1():


def setSalle9():
    salle = Salle(9)
    listes_obstacle = []
    liste_entite = []

    #Genération des obstacle
    #taille obstacle (128,96px)
    #mur 18px

    # murGauche = Rect((0,0),(18, 768))
    # murDroite = Rect((0,1006), (18,768))
    # murHaut = Rect((0,0),(1024,18))
    # murBas = Rect((0,750),(1024,18))
    listes_obstacle.append(Rect((0,0),(18, 768)))
    listes_obstacle.append(Rect((0,1006), (18,768)))
    listes_obstacle.append(Rect((0,0),(1024,18)))
    listes_obstacle.append(Rect((0,750),(1024,18)))
