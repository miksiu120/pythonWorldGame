import random
from Coordinates import Coordinates


class Organism:
    def __init__(self, ourWorld, strength, initiative, x, y, asciiRepresentation, name):
        self.ourWorld = ourWorld
        self.strength = strength
        self.initiative = initiative
        self.asciiRepresentation = asciiRepresentation
        self.name = name
        self.position = Coordinates(x, y)
        self.isOrganismDeleted = False
        self.age = 0

    def action(self):
        pass

    def collision(self, compared):
        if self is None or compared is None:
            return

        if self.getAscii() != compared.getAscii():
            if self.getStrength() < compared.getStrength():
                self.ourWorld.addToKillList(self)
                self.ourWorld.addNewLog(f"{self.name} ginie od {compared.name}")
            else:
                self.ourWorld.addToKillList(compared)
                self.ourWorld.addNewLog(f"{compared.name} ginie od {self.name}")

    def draw(self):
        pass

    def increaseAge(self):
        self.age += 1

    def killOrganism(self):
        self.isOrganismDeleted = True

    def isDeleted(self):
        return self.isOrganismDeleted

    def getEmptyNeighbour(self):
        cords = self.ourWorld.getFromPosition(Coordinates(self.getX(), self.getY() + 1))
        if cords is None and self.canMove(Coordinates(self.getX(), self.getY() + 1)):
            return Coordinates(self.getX(), self.getY() + 1)

        cords = self.ourWorld.getFromPosition(Coordinates(self.getX() + 1, self.getY()))
        if cords is None and self.canMove(Coordinates(self.getX() + 1, self.getY())):
            return Coordinates(self.getX() + 1, self.getY())

        cords = self.ourWorld.getFromPosition(Coordinates(self.getX(), self.getY() - 1))
        if cords is None and self.canMove(Coordinates(self.getX(), self.getY() - 1)):
            return Coordinates(self.getX(), self.getY() - 1)

        cords = self.ourWorld.getFromPosition(Coordinates(self.getX() - 1, self.getY()))
        if cords is None and self.canMove(Coordinates(self.getX() - 1, self.getY())):
            return Coordinates(self.getX() - 1, self.getY())

        return Coordinates(-1, -1)

    def getY(self):
        return self.position.getY()

    def getX(self):
        return self.position.getX()

    def getAscii(self):
        return self.asciiRepresentation

    def getAge(self):
        return self.age

    def getStrength(self):
        return self.strength

    def getInitiative(self):
        return self.initiative

    def getPosition(self):
        return self.position

    def getName(self):
        return self.name

    def setY(self, y):
        self.position.setY(y)

    def setX(self, x):
        self.position.setX(x)

    def setStrength(self, newStrength):
        self.strength = newStrength

    def setAge(self, newAge):
        self.age = newAge

    def setPosition(self, newPosition):
        self.position = newPosition

    def getRandomNeighbour(self):
        direction = random.randint(0, 3)
        if direction == 0:
            return Coordinates(1, 0)
        elif direction == 1:
            return Coordinates(0, 1)
        elif direction == 2:
            return Coordinates(-1, 0)
        else:
            return Coordinates(0, -1)

    def canMove(self, newCoords):
        if (
                self.ourWorld.getTopBorder() <= newCoords.getY() < self.ourWorld.getBottomBorder() and
                self.ourWorld.getLeftBorder() <= newCoords.getX() < self.ourWorld.getRightBorder()
        ):
            return True
        else:
            return False

    def doesDefendItself(self, otherOrganism):
        return self.strength > otherOrganism.getStrength()
