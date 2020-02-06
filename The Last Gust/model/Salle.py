import pygame
from os import *
class Salle:

    def __init__(self, num):
        self.root = path.dirname(__file__)
        self.num = num
        self.image = pygame.image.load(path.join(self.root, "../assets/maps/salle" + str(self.num) + ".png"))
        #list de rectangle dans lesquelle le joueur tombe
        self.liste_trous = []
        self.liste_obstacle = []
        self.liste_entite = []
        self.sortie = 0

    def setSalle(self,liste_trous, liste_obstacle, liste_entite, sortie):
        self.liste_trous = liste_trous
        self.liste_obstacle = liste_obstacle
        self.liste_entite = liste_entite
        self.sortie = sortie

    def peutSortir(self):
        return len(self.liste_entite) == 0
