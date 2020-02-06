import pygame
from os import *
class Salle:

    def __init__(self, num):
        self.root = path.dirname(__file__)
        self.num = num
        self.image = pygame.image.load(path.join(self.root, "../assets/maps/", self.num, ".png"))
        #list de rectangle dans lesquelle le joueur tombe
        self.listes_trous = []
        self.listes_obstacle = []

    def setSalle(listes_trous, listes_obstacle):
        self.listes_trous = listes_trous
        self.listes_obstacle = listes_obstacle

    
