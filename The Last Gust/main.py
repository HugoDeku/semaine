import pygame
import os
from path import*
from Jeu import *

running = True
root = os.path.dirname(__file__)

pygame.init()

pv0 = pygame.transform.scale(pygame.image.load('assets/sprites/plume.png'),(50,50))
pv1 = pygame.transform.scale(pygame.image.load('assets/sprites/plume1.png'),(50,50))
pv2 = pygame.transform.scale(pygame.image.load('assets/sprites/plume2.png'),(50,50))
pv3 = pygame.transform.scale(pygame.image.load('assets/sprites/plume3.png'),(50,50))
pv4 = pygame.transform.scale(pygame.image.load('assets/sprites/plume4.png'),(50,50))
background = pygame.image.load(os.path.join(root, "assets/sprites/bg_temp.png"))


#chargement du jeu
jeu = Jeu()

icone = pygame.image.load('assets/jacket.png')
pygame.display.set_icon(icone)
pygame.display.set_caption("The Last Gust")
ecran = pygame.display.set_mode((1024,768))
myfont = pygame.font.SysFont('Helvetic', 20)

def trieScore(scores):
    retour = []
    while len(scores) > 0:
        meilleur = scores[0]
        for score in scores:
            if int(meilleur[0]) > int(score[0]):
                meilleur = score
        retour.append(meilleur)
        scores.remove(meilleur)
    return retour
def affichageScore():
    fichier = open("score.txt", 'r')
    scores = []
    for ligne in fichier:
        ajout = ligne.replace('\n','')
        scores.append(ajout.split(':'))
    fichier.close()
    scores = trieScore(scores)
    running = True
    while running:
        ecran.blit(pygame.transform.scale(icone, (1024, 768)), (0, 0))
        if 0 < pygame.mouse.get_pos()[0] < 100 and 0 < pygame.mouse.get_pos()[1] < 25:
            couleur = vert_bar
        else:
            couleur = blue_bar
        case = pygame.draw.rect(
            ecran,
            couleur,
            pygame.Rect(0, 0, 100, 25))
        retour = myfont.render('<- Menu', False, (255, 255, 255))
        ecran.blit(retour,
                   (75 - retour.get_width(),
                    18 - retour.get_height()))
        posy = 90
        posx = ecran.get_width() // 2 - 250
        hauteur = 588
        largeur = 500
        pygame.draw.rect(
            ecran,
            blue_bar,
            pygame.Rect(posx, posy, largeur, hauteur))
        i = 0
        while i < 10 and i < len(scores):
            posy += 20
            score = myfont.render(str(i + 1)+ " - " + scores[i][1] + " avec un score de  " + scores[i][0] , False, (255, 255, 255))
            ecran.blit(score,
                       (posx + largeur//4,
                        posy ))
            i += 1

        pygame.display.flip()
        for event in pygame.event.get():
            # event = close window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and couleur == vert_bar:
                running = False
                menu()

#musique

pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load('assets/song/Intro.mp3')
pygame.mixer.music.play(-1)
blue_bar = (0, 102, 153)
vert_bar = (0, 204, 102)
couleur_jouer = blue_bar
couleur_score = blue_bar

#boucle menu d'accueil

def menu():
    menu = True
    while menu:
        ecran.blit(pygame.transform.scale(icone, (1024,768)), (0,0))

        pos_souris = pygame.mouse.get_pos()
        if (200 + ecran.get_width() // 2 - 100 > pos_souris[0] > 200) and (250 > pos_souris[1] > 200):
            couleur_jouer = vert_bar
        else:
            couleur_jouer = blue_bar
        jouer = pygame.draw.rect(
                                ecran,
                                couleur_jouer,
                                pygame.Rect(ecran.get_width()//2 - 100, 200, 200, 50))

        if (200 + ecran.get_width() // 2 - 100 > pos_souris[0] > 200) and (350 > pos_souris[1] > 300):
            couleur_score = vert_bar
        else:
            couleur_score = blue_bar

        score = pygame.draw.rect(
            ecran,
            couleur_score,
            pygame.Rect(ecran.get_width()//2 - 100, 300, 200, 50))

        text_jouer = myfont.render('JOUER', False, (255,255,255))

        text_score = myfont.render('SCORE', False, (255,255,255))

        ecran.blit(text_jouer,
                    (ecran.get_width()//2 - 100 + 100 - text_jouer.get_width()//2,
                    225-text_jouer.get_height() // 2 ))

        ecran.blit(text_score,
                    (ecran.get_width()//2 - 100 + 100 - text_score.get_width()//2,
                    325-text_score.get_height() //2))

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
#boucle jeu

menu()
pygame.mixer.music.load('assets/song/bg_music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

while running:
    #appliquer background
    ecran.blit(background, (0, 0) )

    #appliquer le joueur
    ecran.blit(jeu.joueur.image_actu, jeu.joueur.rect)

    #affichage pdv
    pdv = jeu.joueur.vie
    debut_plume_x = ecran.get_width()//2 - 80
    debut_plume_y = ecran.get_height() - 50
    i = 0
    while i < 3:
        if pdv >= 4:
            ecran.blit(pv4, (debut_plume_x, debut_plume_y))
            pdv -= 4
        elif pdv == 3:
            ecran.blit(pv3, (debut_plume_x, debut_plume_y))
            pdv -= 3
        elif pdv == 2:
            ecran.blit(pv2, (debut_plume_x, debut_plume_y))
            pdv -= 2
        elif pdv == 1:
            ecran.blit(pv1, (debut_plume_x, debut_plume_y))
            pdv -= 1
        else:
            ecran.blit(pv0, (debut_plume_x, debut_plume_y))

        debut_plume_x = debut_plume_x + 55
        i += 1

    for projectile in jeu.joueur.projectiles:
        projectile.deplacement()
        projectile.image = pygame.transform.flip(projectile.image, True, False)
        if projectile.rect.x < 0 or projectile.rect.x > ecran.get_width() or projectile.rect.y < 0 or projectile.rect.y > ecran.get_height():
            jeu.joueur.projectiles.remove(projectile)

    jeu.joueur.projectiles.draw(ecran)

    if jeu.pressed.get(pygame.K_RIGHT):
        jeu.joueur.deplacer_droite(jeu.joueur.rect.x + jeu.joueur.rect.width < ecran.get_width())
    elif jeu.pressed.get(pygame.K_LEFT):
        jeu.joueur.deplacer_gauche(jeu.joueur.rect.x > 0)
    elif jeu.pressed.get(pygame.K_UP):
        jeu.joueur.deplacer_haut(jeu.joueur.rect.y > 0)
    elif jeu.pressed.get(pygame.K_DOWN):
        jeu.joueur.deplacer_bas(jeu.joueur.rect.y + jeu.joueur.rect.height < ecran.get_height())

    if not jeu.pressed.get(pygame.K_RIGHT) and not jeu.pressed.get(pygame.K_LEFT) and not jeu.pressed.get(pygame.K_UP) and not jeu.pressed.get(pygame.K_DOWN) :
        jeu.joueur.arret_deplacement()

    #maj ecran
    pygame.display.flip()

    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        #event = close window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #detecter lorque qu'un joueur presse une touche
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                effect = pygame.mixer.Sound('assets/song/wind_effect.wav')
                effect.set_volume(0.3)
                jeu.joueur.lance_projectile(effect)
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False

    pygame.time.Clock().tick(120)
