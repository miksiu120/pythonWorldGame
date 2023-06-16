import random
from Plant import Plant

class Dandelion(Plant):


    def __init__(self, ourWorld, posX, posY, strength = 0, initative = 0,age=0):
        self.age = age
        super().__init__(ourWorld, strength, initative, posX, posY, 'D', 5, "Mlecz")

    def action(self):
        for i in range(3):
            super().action()
