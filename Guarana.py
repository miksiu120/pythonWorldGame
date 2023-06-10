from Plant import Plant
from Coordinates import Coordinates
from Animal import Animal
class Guarana(Plant):
    SPAWN_RATIO = 5



    def __init__(self, ourWorld, posX, posY, strength = 0, initative = 0):

        super().__init__(ourWorld, strength, initative, posX, posY, 'U', 5, "Guarana")

    def collision(self, element):
        animal = element if isinstance(element, Animal) else None
        if animal is not None:
            element.setStrength(element.getStrength() + 3)
        super().collision(element)
