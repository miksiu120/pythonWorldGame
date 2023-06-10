import random
from Organism import Organism
from Coordinates import Coordinates
class Plant(Organism):
    DEFAULT_SPAWN_RATIO = 5

    def __init__(self, world, strength, initiative, x, y, symbol, spawnRatio, name):
        super().__init__(world, strength, initiative, x, y, symbol, name)
        self.SPAWN_RATIO = spawnRatio




    def doesSpread(self):
        return random.randint(0, 99) < self.SPAWN_RATIO

    def action(self):
        if self.doesSpread():
            moveTo = self.getRandomNeighbour()
            newCoords = Coordinates(self.getX() + moveTo.getX(), self.getY() + moveTo.getY())
            if self.canMove(newCoords) and self.ourWorld.getFromPosition(newCoords) is None:
                newPlant = Plant(self)
                newPlant.setPosition(newCoords)
                newPlant.setAge(0)
                self.ourWorld.addNewElementToWorld(newPlant)
