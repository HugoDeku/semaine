import pygame
import os

class Entite(pygame.sprite.Sprite):

    #Constructeur de la class Entite
    def __init__(self, nom):
        self.root = os.path.dirname(__file__)
        super().__init__()
        self.nom = nom
        self.vie = 1
        self.velocite = 1
        self.path = "../assets/sprites/" + self.nom
        self.listes_sprites = {}
        self.image_actu = 0
        self.rect = 0
        self.direction ="bas"
        self.degats = 0
        #facteur multiplicateur de distance
        self.dist_Attaque = 50

    def estMort(self):
        if self.vie <= 0:
            return True

    def attaque(self):
        pass

    def mourir(self, liste_entite):
        liste_entite.remove(self)
    
    def set_sprite(self, posx, posy):
        self.listes_sprites = {
            "haut": pygame.image.load(os.path.join(self.root, self.path) + "_haut.png"),
            "mouvement_haut": pygame.image.load(os.path.join(self.root, self.path)+'_mouvHaut.png'),
        }
        self.listes_sprites.update({'bas': pygame.transform.rotate(self.listes_sprites["haut"], 180)})
        self.listes_sprites.update({'bas':pygame.transform.rotate(self.listes_sprites["haut"], 180)})
        self.listes_sprites.update({'mouvement_bas': pygame.transform.rotate(self.listes_sprites["mouvement_haut"], 180)})
        self.listes_sprites.update({'droite':  pygame.transform.rotate(self.listes_sprites["haut"], 270)})
        self.listes_sprites.update({'mouvement_droite':  pygame.transform.rotate(self.listes_sprites["mouvement_haut"], 270)})
        self.listes_sprites.update({'gauche': pygame.transform.rotate(self.listes_sprites["haut"], 90)})
        self.listes_sprites.update({'mouvement_gauche': pygame.transform.rotate(self.listes_sprites["mouvement_haut"], 90)})

        self.image_actu = self.listes_sprites["bas"]
        self.rect = self.image_actu.get_rect()
        self.rect.x = posx
        self.rect.y = posy



    def deplacer_droite(self, possible = True):
        self.changement_sprite("mouvement_droite")
        if possible:
            self.rect.x += self.velocite
        self.direction = "droite"

    def deplacer_haut(self, possible = True):
        self.changement_sprite("mouvement_haut")
        if possible:
            self.rect.y -= self.velocite
        self.direction = "haut"

    def deplacer_bas(self, possible = True):
        self.changement_sprite("mouvement_bas")
        if possible:
            self.rect.y += self.velocite
        self.direction = "bas"

    def deplacer_gauche(self, possible = True):
        self.changement_sprite("mouvement_gauche")
        if possible:
            self.rect.x -= self.velocite
        self.direction = "gauche"

    def arret_deplacement(self):
        self.changement_sprite(self.direction)

    def changement_sprite(self, nom):
        x = self.rect.x
        y = self.rect.y
        self.image_actu = self.listes_sprites[nom]
        self.rect = self.image_actu.get_rect()
        self.rect.x = x
        self.rect.y = y

    def subirDegats(self, degats):
        self.vie -= degats

    def infligeDegat(self, entite):
        entite.subirDegats(entite.degats)

    def followPlayer(self, joueur):
        print(self.peutAttaquer(joueur))
        if not self.peutAttaquer(joueur):

            dist_X = abs(self.rect.x - joueur.rect.x)
            dist_Y = abs(self.rect.y - joueur.rect.y)

            if dist_X >= dist_Y:
                self.deplacer_droite() if (self.rect.x <= joueur.rect.x) else self.deplacer_gauche()
            else:
                self.deplacer_bas() if (self.rect.y <= joueur.rect.y) else self.deplacer_haut()

    def peutAttaquer(self, joueur):
        if (joueur.rect.x < self.rect.x + self.rect.width//2 and self.rect.x + self.rect.width//2 < joueur.rect.x + joueur.rect.width) and (abs(self.rect.y - joueur.rect.y) <= self.dist_Attaque):
            self.attaque()
            return True
        elif (joueur.rect.y < self.rect.y + self.rect.height//2 and self.rect.y + self.rect.height//2 < joueur.rect.y + joueur.rect.height) and (abs(self.rect.x - joueur.rect.x) <= self.dist_Attaque):
            self.attaque()
            return True
        else:
            return False

    def collisionObstacle(self, liste_obstacles):
        #retourne bas haut gauche droite ou non en fonction de si il y a une collision et de la direction de la collision
        for rect in liste_obstacles:
            if self.rect.colliderect(rect):
                if self.rect.x <= rect.x+rect.width :
                    return "gauche"

                elif self.rect.x+ self.rect.width >= rect.x:
                    return "droite"

                elif self.rect.y <= rect.y+rect.height:
                    return "haut"

                else:
                    return "bas"

            else:
                return "non"


    def collisionProjectile(self, liste_projectiles,liste_entites,liste_obstacles):
        subitdegats = False
        for projectile in liste_projectiles:
            if self.rect.colliderect(projectile.rect):
                if projectile.nom == "tornade":
                    projectile.supprimer()
                    if projectile.direction == "haut":
                        i=0
                        while i <5 and cobstacles == "non" and centite == "non":
                            centite = self.collisionEntite(liste_entites)
                            cobstacles = self.collisionObstacles
                            deplacer_haut()
                            i+=1
                    elif projectile.direction== "bas":
                        i=0
                        while i <5 and cobstacles == "non" and centite == "non":
                            centite = self.collisionEntite(liste_entites)
                            cobstacles = self.collisionObstacles
                            deplacer_bas()
                            i+=1
                    elif projectile.direction=="gauche":
                        i=0
                        while i <5 and cobstacles == "non" and centite == "non":
                            centite = self.collisionEntite(liste_entites)
                            cobstacles = self.collisionObstacles
                            deplacer_gauche()
                            i+=1
                    else:
                        i=0
                        while i <5 and cobstacles == "non" and centite == "non":
                            centite = self.collisionEntite(liste_entites)
                            cobstacles = self.collisionObstacles
                            deplacer_droite()
                            i+=1
                else :
                    projectile.infligedegats(self)
                    subitdegats = True            
        return subitDegats

    def collisionEntite(self, liste_entites):
        for entite in liste_entites:
            if self.rect.colliderect(entite.rect):
                if self.rect.x <= entite.rect.x+entite.rect.width :
                    return "gauche"

                elif self.rect.x+ self.rect.width >= entite.rect.x:
                    return "droite"

                elif self.rect.y <= entite.rect.y+entite.rect.height:
                    return "haut"

                else:
                    return "bas"

            else:
                return "non"


    def collisionTrou(self, liste_trous):
        for rect in liste_trous:
            if self.rect.colliderect(rect):
                self.mourir()

        
        
