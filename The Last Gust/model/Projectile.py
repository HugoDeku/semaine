    class Projectile():

        def __init(self, nom, degats, velocite, direction, posx, posy):
            super().__init__();
            self.degats = degats
            self.velocite = velocite
            self.direction = direction
            self.nom = nom
            self.rect = self.image_actu.get_rect()
            self.rect.x = posx
            self.rect.y = posy

        def deplacement(self):
            if self.direction = "bas":
               self.rect.y += self.velocite
            elif self.direction = "haut":
                self.rect.y -= self.velocite
            elif self.direction = "gauche":
                self.rect.x -= self.velocite
            else :
                self.rect.x += self.velocite

        def infligeDegats(self,joueur):
            joueur.vie -= self.degats
