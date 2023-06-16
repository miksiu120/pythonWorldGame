from Organism import Organism
from Coordinates import Coordinates
class Animal(Organism):
    def __init__(self, ourWorld, strength, initiative, x, y, asciiRep, animal):
        super().__init__(ourWorld, strength, initiative, x, y, asciiRep, animal)

    def action(self, moveTo=None):
        if moveTo is None:
            moveTo = self.getRandomNeighbour()

        newCoords = Coordinates(self.getX() + moveTo.getX(), self.getY() + moveTo.getY())
        organismOnNewCoords = self.ourWorld.getFromPosition(newCoords)

        if self.canMove(newCoords) and organismOnNewCoords is None:
            self.setX(newCoords.getX())
            self.setY(newCoords.getY())
        elif organismOnNewCoords is not None:
            organismOnNewCoords.collision(self)

    def collision(self, collidedElement):
        super().collision(collidedElement)
        if collidedElement is None or self is None:
            return
        self.tryCopulate(collidedElement)

    def tryCopulate(self, potentialSame):
        sameAnimal = potentialSame if isinstance(potentialSame, Animal) else None
        if sameAnimal is None:
            return
        if self.getAscii() == sameAnimal.getAscii() and self.getAge() > 10 and sameAnimal.getAge() > 10:
            if self.tryBornNewAnimal():
                return
            if sameAnimal.tryBornNewAnimal():
                return

    def tryBornNewAnimal(self):
        newOrganism = Animal(self.ourWorld, self.getStrength(), self.getInitiative(), -1, -1, self.getAscii(), self.getName())
        positionOfNewElement = self.getEmptyNeighbour()
        if positionOfNewElement.getX() != -1 and positionOfNewElement.getY() != -1:
            newOrganism.setPosition(positionOfNewElement)
            self.ourWorld.addNewLog("Kopulacja " + self.getName() + " nowe zwierze (" +
                                    str(positionOfNewElement.getX()) + ", " + str(positionOfNewElement.getY()) + ")")
            newOrganism.setAge(0)
            self.setAge(3)
            self.ourWorld.addNewElementToWorld(newOrganism)
            return True
        else:
            return False
