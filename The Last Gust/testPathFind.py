import pygame
from pygame.locals import *
import path
from Boss import *
from Joueur import *

pygame.init()

fenetre = pygame.display.set_mode((500,500))

p1 = Boss()
joueur = Joueur(0,100)
fond = pygame.image.load(path.join(path.dirname(__file__),"assets/sprites/bg_temp.png"))


ite = 0
while 1:
    fenetre.blit(fond, (0,0))
    fenetre.blit(p1.image_actu, p1.rect)
    fenetre.blit(joueur.image_actu, joueur.rect)
    pygame.display.flip()
    if ite == 4:
        p1.followPlayer(joueur)
        ite = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    ite += 1
    pygame.time.Clock().tick(120)
