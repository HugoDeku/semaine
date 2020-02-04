import pygame
from pygame.locals import *
import sys

sys.path.append('./class/')
sys.path.append('./class/Boss')
sys.path.append('./class/Entite')
from Boss import *
from Entite import *

boss = Boss()
entity = Entite()

print(str(boss.vie))
print(str(entity.vie))
