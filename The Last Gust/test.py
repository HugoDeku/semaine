import pygame
from pygame.locals import *
import sys

sys.path.append('./model/')
sys.path.append('./model/Boss')
sys.path.append('./model/Entite')
from Boss import *
from Entite import *

fenetre = pygame.display.set_mode((500,500))

perso = Boss()

fenetre.blit(perso.image_actu, perso.rect)
fenetre.flip()
while 1:
    continue
