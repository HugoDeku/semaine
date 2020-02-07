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
        self.cooPorteSuivante = []
        self.cooPortePrecedente = []
        self.sortie = 0

    def setSalle(self,liste_trous, liste_obstacle, liste_entite, sortie):
        self.liste_trous = liste_trous
        self.liste_obstacle = liste_obstacle
        self.liste_entite = liste_entite
        self.sortie = sortie


    def peutSortir(self):
        return len(self.liste_entite) == 0

    def setSuivant(self,coo ,numsalle):
        self.cooPorteSuivante = coo
        self.suivante = numsalle

    def setPrecedente(self,coo ,numsalle):
        self.cooPortePrecedente = coo
        self.precedente = numsalle

    def sort(self, player):
        if 'cooPorteSuivante' in self.__dict__ and self.contactSuivante(player):
            return self.suivante
        elif 'cooPortePrecedente' in self.__dict__ and self.contactPrecedente(player):
            return self.precedente
        else:
            return -1
    def contactSuivante(self, player):
        return (self.cooPorteSuivante[0]<player.rect.x + player.rect.width//2< self.cooPorteSuivante[0] + self.cooPorteSuivante[2] and self.cooPorteSuivante[1]<player.rect.y + player.rect.height//2< self.cooPorteSuivante[1] + self.cooPorteSuivante[3] )

    def contactPrecendente(self, player):
        return (self.cooPortePrecedentee[0]<player.rect.x + player.rect.width//2< self.cooPortePrecedente[0] + self.cooPortePrecedente[2] and self.cooPortePrecedente[1]<player.rect.y + player.rect.height//2< self.cooPortePrecedente[1] + self.cooPortePrecedente[3] )
