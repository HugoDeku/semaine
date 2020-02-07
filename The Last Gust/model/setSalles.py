import pygame
from pygame import Rect
import path
from Salle import *
from Boss import *
from Lance import *
from Fronde import *

#taille obstacle (128,96px)
#mur 18px
#troue 10px de moins coté sol

# murGauche = Rect((0,0),(18, 768))
# murDroite = Rect((0,1006), (18,768))
# murHaut = Rect((0,0),(1024,18))
# murBas = Rect((0,750),(1024,18))

def takeMap(numSalle):
    listeMap = {1 : setSalle1(),
            2 : setSalle2(),
            9 : setSalle9()}
    return listeMap[numSalle]

def setSalle1():
    salle = Salle(1)
    liste_trous = []
    liste_obstacle = []
    liste_entite = []
    largeur = 128
    hauteur = 96
    taille_mur = (largeur,hauteur)

    #porteSuivante salle


    #Génération des troueeees
    #Coin de la salle
    liste_trous.append(Rect((0*largeur, 0*hauteur), taille_mur))
    liste_trous.append(Rect((7*largeur, 0*hauteur), taille_mur))
    liste_trous.append(Rect((0*largeur, 7*hauteur), taille_mur))
    liste_trous.append(Rect((7*largeur, 7*hauteur), taille_mur))
    #centre de la salle
    liste_trous.append(Rect((3*largeur, 3*hauteur), (2*largeur, 2*hauteur)))
    liste_trous.append(Rect((3*largeur+10,2*hauteur+10), (2*largeur-20, 1*hauteur-10)))
    liste_trous.append(Rect((2*largeur+10, 3*hauteur+10), (1*largeur-10, 2*hauteur-20)))
    liste_trous.append(Rect((4*largeur, 2*hauteur+10), (1*largeur-10, 2*hauteur-20)))
    liste_trous.append(Rect((3*largeur+10, 5*hauteur), (2*largeur-20, 1*hauteur-10)))
    #bande de trous
    #gauche / droite
    liste_trous.append(Rect((0*largeur, 0*hauteur), (1*largeur-10, 8*hauteur)))
    liste_trous.append(Rect((7*largeur+10, 0*hauteur), (1*largeur-10, 8*hauteur)))

    #haut
    liste_trous.append(Rect((0*largeur, 0*hauteur), (4*largeur-10, 1*hauteur-10)))
    liste_trous.append(Rect((5*largeur+10, 0*hauteur), (3*largeur-10, 1*hauteur-10)))
    #Bas
    liste_trous.append(Rect((0*largeur, 7*hauteur+10), (3*largeur-10, 1*hauteur-10)))
    liste_trous.append(Rect((4*largeur+10, 7*hauteur+10), (4*largeur-10, 1*hauteur-10)))

    #Génération des obstacles
    liste_obstacle.append(Rect((0*largeur,0*hauteur),(18, 768)))
    liste_obstacle.append(Rect((8*largeur-18,0*hauteur), (18,768)))
    liste_obstacle.append(Rect((0*largeur,0*hauteur),(1024,18)))
    liste_obstacle.append(Rect((0*largeur,8*hauteur-18),(1024,18)))

    #Génération entite
    liste_entite.extend([Lance(2*largeur-25, 2*hauteur-70),
                         Lance(6*largeur-25, 2*hauteur-70),
                         Lance(2*largeur-25, 6*hauteur-70),
                         Lance(6*largeur-25, 6*hauteur-70)])

    salle.setSalle(liste_trous, liste_obstacle, liste_entite, None)
    return salle
def setSalle2():
    salle = Salle(2)
    liste_trous = []
    liste_obstacle = []
    liste_entite = []
    largeur = 128
    hauteur = 96

    #Génération des trous
    liste_trous.append(Rect((0*largeur, 0*hauteur), (3*largeur-10, 1*hauteur-10)))
    liste_trous.append(Rect((0*largeur, 1*hauteur), (2*largeur-10, 1*hauteur-10)))
    liste_trous.append(Rect((0*largeur, 2*hauteur), (1*largeur-10, 1*hauteur-10)))

    liste_trous.append(Rect((3*largeur+10, 3*hauteur+10), (2*largeur-20, 1*hauteur-20)))

    liste_trous.append(Rect((5*largeur+10, 5*hauteur+10), (1*largeur-20, 2*hauteur-20)))
    liste_trous.append(Rect((6*largeur, 6*hauteur-10), (1*largeur-10, 1*hauteur-20)))

    #Genération des obstacle
    liste_obstacle.append(Rect((0*largeur,0*hauteur),(18, 768)))
    liste_obstacle.append(Rect((8*largeur-18,0*hauteur), (18,768)))
    liste_obstacle.append(Rect((0*largeur,0*hauteur),(1024,18)))
    liste_obstacle.append(Rect((0*largeur,8*hauteur-18),(1024,18)))
    liste_obstacle.append(Rect((1*largeur,5*hauteur), (2*largeur, 1*hauteur)))
    liste_obstacle.append(Rect((5*largeur, 1*hauteur), (1*largeur, 2*hauteur)))

    #génération des entités
    liste_entite.extend([Fronde(0*largeur, 0*hauteur),
                         Fronde(8*largeur, 0*hauteur),
                         Fronde(6*largeur+50, 5*hauteur)])
    salle.setSalle(liste_trous, liste_obstacle, liste_entite, None)
    return salle

def setSalle9():
    salle = Salle(9)
    liste_trous = []
    liste_obstacle = []
    liste_entite = []
    largeur = 128
    hauteur = 96
    taille_mur = (largeur,hauteur)
    #Genération des obstacle

    liste_obstacle.append(Rect((0*largeur,0*hauteur),(18, 768)))
    liste_obstacle.append(Rect((8*largeur-18,0*hauteur), (18,768)))
    liste_obstacle.append(Rect((0*largeur,0*hauteur),(1024,18)))
    liste_obstacle.append(Rect((0*largeur,8*hauteur-18),(1024,18)))


    liste_obstacle.append(Rect((0*largeur, 0*hauteur), taille_mur))
    liste_obstacle.append(Rect((7*largeur, 0*hauteur), taille_mur))
    liste_obstacle.append(Rect((2*largeur, 1*hauteur), taille_mur))
    liste_obstacle.append(Rect((5*largeur, 1*hauteur), taille_mur))
    liste_obstacle.append(Rect((1*largeur, 2*hauteur), taille_mur))
    liste_obstacle.append(Rect((6*largeur, 2*hauteur), taille_mur))
    liste_obstacle.append(Rect((1*largeur, 5*hauteur), taille_mur))
    liste_obstacle.append(Rect((6*largeur, 5*hauteur), taille_mur))
    liste_obstacle.append(Rect((2*largeur, 6*hauteur), taille_mur))
    liste_obstacle.append(Rect((5*largeur, 6*hauteur), taille_mur))
    liste_obstacle.append(Rect((0*largeur, 7*hauteur), taille_mur))
    liste_obstacle.append(Rect((7*largeur, 7*hauteur), taille_mur))

    #Génération des entités
    liste_entite.append(Boss())
    salle.setSalle(liste_trous, liste_obstacle, liste_entite, None)
    return salle
