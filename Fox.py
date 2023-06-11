from Animal import Animal
from Coordinates import Coordinates
class Fox(Animal):


    def __init__(self, ourWorld, posX, posY, strength = 3, initative = 7):
        self.strength = strength
        self.initative = initative
        super().__init__(ourWorld, self.strength, self.initative, posX, posY, 'F', "Lis")

    def action(self):
        moveTo = self.getRandomNeighbour()
        newCoords = Coordinates(self.getX() + moveTo.getX(), self.getY() + moveTo.getY())
        organismOnNewCoords = self.ourWorld.getFromPosition(newCoords)

        if self.canMove(newCoords) and organismOnNewCoords is None:
            self.setX(newCoords.getX())
            self.setY(newCoords.getY())
        elif organismOnNewCoords is not None and organismOnNewCoords.getStrength() <= self.getStrength():
            self.collision(organismOnNewCoords)

    def doesHaveMoreStrength(self, other):
        return other.getStrength() < self.getStrength()
