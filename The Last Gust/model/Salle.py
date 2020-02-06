import pygame
from os import *
class Salle:

    def __init__(self, num):
        self.root = path.dirname(__file__)
        self.num = num
        self.image = pygame.image.load(path.join(self.root, "../assets/maps/salle", self.num, ".png"))
        #list de rectangle dans lesquelle le joueur tombe
        self.liste_trous = []
        self.liste_obstacle = []
        self.liste_entite = []

    def setSalle(liste_trous, liste_obstacle, liste_entite):
        self.liste_trous = listes_trous
        self.liste_obstacle = listes_obstacle
        self.liste_entite = liste_entite
