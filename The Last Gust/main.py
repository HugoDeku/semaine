import pygame
import os
from path import*
from Jeu import *
from time import time
import codecs
from setSalles import *
from Salle import *

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
myfont = pygame.font.SysFont('constantia', 20)

def credits():
    credits_lignes = []
    with codecs.open("credits.txt", 'r',encoding="utf-8") as fichier:
        for line in fichier:
            ligne = line.replace('\n', '')
            credits_lignes.append(ligne)
            if'str' in line:
                break


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
        pygame.draw.rect(ecran,blue_bar,pygame.Rect(posx, posy, largeur, hauteur))
        posy = posy +20
        i = 0
        while i < len(credits_lignes):
            crd = myfont.render(credits_lignes[i], False, (255, 255, 255))
            ecran.blit(crd, (posx+20, posy))
            i = i + 1
            posy += 50


        pygame.display.flip()
        for event in pygame.event.get():
            # event = close window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and couleur == vert_bar:
                running = False
                menu()
    pass

def decoupageIntro(lignes, fichier, taille_ligne = 100):
    texte = fichier.read()
    texte = texte.replace('\n', ' ')
    buffer = ""
    i = 0

    for c in texte:
        if i < taille_ligne or (not c== ' ' and not c == '.'):
            buffer = buffer + c
            i+=1
        else:
            lignes.append(buffer)
            buffer = ""
            i=0
    return lignes

def intro():
    fichier = codecs.open("intro.txt","r", encoding="utf-8")
    lignes = []
    lignes = decoupageIntro(lignes, fichier)
    fichier.close
    fond_noir = pygame.image.load("assets/sprites/fond_noir.jpg")
    running = True
    hauteur = 50
    decalage = 768
    temps = None
    while running:
        ecran.blit(fond_noir, (0, 0))
        passer = myfont.render("Appuyer sur espace pour passer l'introduction", False , (255, 255 ,255))
        ecran.blit(passer, (0,0))
        i = 0
        while i < len(lignes):
            ligne_ecran = myfont.render(lignes[i], False, (255, 255, 255))
            ecran.blit(ligne_ecran,
                        (ecran.get_width()//2 - ligne_ecran.get_width() // 2, i * hauteur + decalage))
            i += 1
        pygame.display.flip()
        for event in pygame.event.get():
            # event = close window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                jeu.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    running = False
        if decalage > ecran.get_height() // 4:
            decalage -= 1
        elif temps is None:
            temps = time()

        if not temps is None:
            if time() - temps > 10:
                running = False
        pygame.time.Clock().tick(120)




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


intro()


pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load('assets/song/Intro.mp3')
pygame.mixer.music.play(-1)
blue_bar = (0, 102, 153)
vert_bar = (0, 204, 102)

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

        if (200 + ecran.get_width() // 2 - 100 > pos_souris[0] > 200) and (450 > pos_souris[1] > 400):
            couleur_credits = vert_bar
        else:
            couleur_credits = blue_bar

        credits_menu = pygame.draw.rect(
            ecran,
            couleur_credits,
            pygame.Rect(ecran.get_width()//2 - 100, 400, 200, 50))

        text_jouer = myfont.render('JOUER', False, (255,255,255))

        text_score = myfont.render('SCORE', False, (255,255,255))

        text_credits = myfont.render('CREDITS', False, (255,255,255))

        ecran.blit(text_jouer,
                    (ecran.get_width()//2 - 100 + 100 - text_jouer.get_width()//2,
                    225-text_jouer.get_height() // 2 ))

        ecran.blit(text_score,
                    (ecran.get_width()//2 - 100 + 100 - text_score.get_width()//2,
                    325-text_score.get_height() //2))

        ecran.blit(text_credits,
                   (ecran.get_width() // 2 - 100 + 100 - text_credits.get_width() // 2,
                    425 - text_credits.get_height() // 2))

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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and couleur_credits == vert_bar:
                credits()
                menu = False
#boucle jeu

menu()
pygame.mixer.music.load('assets/song/bg_music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

numMap = 1
salle = Salle(2)
while running:
    #appliquer background
    ecran.blit(background, (0, 0) )

    #générer la bonne map
    if not salle.num == numMap:
        salle = takeMap(numMap)
        background = salle.image
        #génére les mob sur map
    for mobs in salle.liste_entite:
        ecran.blit(mobs.image_actu, mobs.rect)



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
    #Gestion projectile joueur
    for projectile in jeu.joueur.projectiles:
        projectile.deplacement()
        projectile.image = pygame.transform.flip(projectile.image, True, False)
        if projectile.rect.x + projectile.rect.width < 0 or projectile.rect.x > ecran.get_width() or projectile.rect.y + projectile.rect.height < 0 or projectile.rect.y > ecran.get_height():
            jeu.joueur.projectiles.remove(projectile)

    jeu.joueur.projectiles.draw(ecran)

    #Déplacement joueur
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

    #Gestion Salles

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
