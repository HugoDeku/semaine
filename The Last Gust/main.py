import pygame
from pygame.locals import *
import path

fenetre = pygame.display.set_mode((1024,768))
pygame.display.flip()

principale = 0
while not principale:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
