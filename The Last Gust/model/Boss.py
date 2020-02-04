from Entite import *

class Boss(Entite):

    def __init__(self):
        super().__init__("Boss")
        self.vie = 50
        self.velocite = 2
        super().set_sprite(10, 10)
