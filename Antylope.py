from random import random
from Animal import Animal

class Antylope(Animal):

    def __init__(self, ourWorld, posX, posY, strength = 4, initative = 4,age=0):
        self.age = age
        super().__init__(ourWorld, strength, initative, posX, posY, 'T', "Antylopa")

    def action(self):
        super().action()
        super().action()

    def collision(self, attacker):
        if attacker is None or self is None:
            return

        animal = attacker if isinstance(attacker, Animal) else None
        self.tryCopulate(animal)

        if random() < 0.5:
            super().collision(attacker)
        else:
            newCords = self.getEmptyNeighbour()
            if newCords.getX() != -1 and newCords.getY() != -1:
                self.setPosition(newCords)
