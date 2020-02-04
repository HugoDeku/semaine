from Entite import *


class Rocher():

    def __init__(self, nom, posx, posy):
        super().__init__()
        self.nom = nom
        self.rect.x = posx
        self.rect.y = posy
        self.velocite = 2

    def deplacement(self, direction):
        if direction == "bas":
            self.rect.y += self.velocite
        elif direction == "haut":
            self.rect.y -= self.velocite
        elif direction == "gauche":
            self.rect.x -= self.velocite
        else:
            self.rect.x += self.velocite

    def aubonendroit(self, x, y):
        if x + 50 > self.posx > x - 50 and y - 50 > self.posy > y + 50:
            return True
        else:
            return False
