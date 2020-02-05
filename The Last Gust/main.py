import pygame
from os import *
import path
from Jeu import *

running = True
root = path.dirname(__file__)

pygame.init()

pv0 = pygame.transform.scale(pygame.image.load('assets/sprites/plume.png'),(50,50))
pv1 = pygame.transform.scale(pygame.image.load('assets/sprites/plume1.png'),(50,50))
pv2 = pygame.transform.scale(pygame.image.load('assets/sprites/plume2.png'),(50,50))
pv3 = pygame.transform.scale(pygame.image.load('assets/sprites/plume3.png'),(50,50))
pv4 = pygame.transform.scale(pygame.image.load('assets/sprites/plume4.png'),(50,50))
background = pygame.image.load(path.join(root, "assets/sprites/bg_temp.png"))


#chargement du jeu
jeu = Jeu()

#musique

pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load('assets/song/bg_music.mp3')
pygame.mixer.music.play(-1)

icone = pygame.image.load('assets/jacket.png')
pygame.display.set_icon(icone)
pygame.display.set_caption("The Last Gust")
ecran = pygame.display.set_mode((1024,768))



#boucle jeu

while running:
    #appliquer background
    ecran.blit(background, (0, 0) )

    #appliquer le joueur
    ecran.blit(jeu.joueur.image_actu, jeu.joueur.rect)

    #affichage pdv
    pdv = jeu.joueur.vie
    debut_plume_x = ecran.get_width()/2 - 80
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