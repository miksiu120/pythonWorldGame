from Coordinates import Coordinates

from typing import List
from Organism import Organism
from Plant import Plant

class SosnowskiBarszcz(Plant):
    SPAWN_RATIO = 57

    def __init__(self, ourWorld, posX, posY, strength=10, initative=0, age=0):
        self.age = age
        super().__init__(ourWorld, strength, initative, posX, posY, '0', 57, "Barszcz sosnowskiego")

    def action(self):
        nearbyArea: List[Organism] = [
            self.ourWorld.getFromPosition(Coordinates(self.getX(), self.getY() - 1)),
            self.ourWorld.getFromPosition(Coordinates(self.getX(), self.getY() + 1)),
            self.ourWorld.getFromPosition(Coordinates(self.getX() - 1, self.getY())),
            self.ourWorld.getFromPosition(Coordinates(self.getX() + 1, self.getY())),
            self.ourWorld.getFromPosition(Coordinates(self.getX() + 1, self.getY() + 1)),
            self.ourWorld.getFromPosition(Coordinates(self.getX() + 1, self.getY() - 1)),
            self.ourWorld.getFromPosition(Coordinates(self.getX() - 1, self.getY() + 1)),
            self.ourWorld.getFromPosition(Coordinates(self.getX() - 1, self.getY() - 1))
        ]

        for org in nearbyArea:
            if org is not None:
                self.ourWorld.addToKillList(org)
