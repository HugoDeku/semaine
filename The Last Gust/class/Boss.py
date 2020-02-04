from Entite import *

class Boss(Entite):

    def __init__(self):
        super().__init__()
        self.vie = 50
        self.velocite = 2
        self.sprite = {}
