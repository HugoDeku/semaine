import pygame
import sys
from Joueur import *

class Jeu:

    def __init__(self):
        self.joueur = Joueur(0,0)
        self.pressed = {}