import random
from Animal import Animal
class Turtle(Animal):

    def __init__(self, ourWorld, posX, posY):
        super().__init__(ourWorld, 2, 1, posX, posY, 'T', "Zolw")

    def __init__(self, ourWorld, posX, posY, strength = 2, initative = 1):
        super().__init__(ourWorld, strength, initative, posX, posY, 'T', "Zolw")

    def action(self):
        if random.randint(0, 3) == 1:
            super().action()

    def collision(self, element):
        if element is None or self is None:
            return
        if element.getStrength() >= 5:
            super().collision(element)
        else:
            self.tryCopulate(element)
