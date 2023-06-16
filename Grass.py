import random
from Plant import Plant
from Coordinates import Coordinates


class Grass(Plant):
    SPAWN_RATIO = 5

    def __init__(self, ourWorld, posX, posY, strength=0, initative=0,age=0):
        self.age = age
        super().__init__(ourWorld, strength, initative, posX, posY,  'G', 5,"Trawa")
        self.rand = random.Random()

    def action(self):
        if self.doesSpread(self.SPAWN_RATIO):
            moveTo = self.getRandomNeighbour()
            newCoords = Coordinates(self.getX() + moveTo.getX(), self.getY() + moveTo.getY())
            if self.canMove(newCoords) and self.ourWorld.getFromPosition(newCoords) is None:
                newElement = Grass(self.ourWorld, newCoords.getX(), newCoords.getY())
                self.ourWorld.addNewElementToWorld(newElement)

    def doesSpread(self, spawnRatio):
        return self.rand.randint(0, 99) < spawnRatio
