import pygame
import os
from path import*
from Jeu import*

running = True
root = os.path.dirname(__file__)

pygame.init()

pv0 = pygame.transform.scale(pygame.image.load('assets/sprites/plume.png'),(50,50))
pv1 = pygame.transform.scale(pygame.image.load('assets/sprites/plume1.png'),(50,50))
pv2 = pygame.transform.scale(pygame.image.load('assets/sprites/plume2.png'),(50,50))
pv3 = pygame.transform.scale(pygame.image.load('assets/sprites/plume3.png'),(50,50))
pv4 = pygame.transform.scale(pygame.image.load('assets/sprites/plume4.png'),(50,50))
background = pygame.image.load(os.path.join(root, "assets/sprites/bg_temp.png"))

jeu = Jeu()

icone = pygame.image.load('assets/jacket.png')
pygame.display.set_icon(icone)
pygame.display.set_caption("The Last Gust")

ecran = pygame.display.set_mode((1024,768))
myfont = pygame.font.SysFont('Helvetic', 20)

def menu():
    menu = True
    while menu:
        ecran.blit(pygame.transform.scale(icone, (1024,768)), (0,0))

        pos_souris = pygame.mouse.get_pos()
        if (200 + ecran.get_width() // 2 - 100 > pos_souris[0] > 200) and (350 > pos_souris[1] > 200):
            jouer = pygame.image.load('assets/intro/jouer_pressed.png')
        else:
            jouer = pygame.image.load('assets/intro/jouer_unpressed.png')
        if (200 + ecran.get_width() // 2 - 100 > pos_souris[0] > 200) and (550 > pos_souris[1] > 400):
            score = pygame.image.load('assets/intro/scores_pressed.png')
        else:
            score = pygame.image.load('assets/intro/scores_unpressed.png')

        ecran.blit(jouer,(ecran.get_width()//2 - 100 + 100 - jouer.get_width()//2,
                    225-jouer.get_height() // 2 ))
        ecran.blit(score,(ecran.get_width()//2 - 100 + 100 - score.get_width()//2,
        500-score.get_height() //2))
        print(jouer.get_rect()[0])
        print(jouer.get_rect().y + jouer.get_height() + 20)
        pygame.display.flip()
        for event in pygame.event.get():
            #event = close window
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and couleur_jouer == vert_bar:
                menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and couleur_score == vert_bar:
                affichageScore()
                menu = False

menu()
