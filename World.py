
from Coordinates import Coordinates
from importsOrganisms import *
import random
class World:
    def __init__(self, worldWidth,worldHeight):
        self.worldWidth = worldWidth
        self.worldHeight = worldHeight
        self.mapSize = Coordinates(worldWidth, worldHeight)
        self.TOP_BORDER = worldHeight
        self.BOTTOM_BORDER = worldWidth
        self.organisms = []
        self.killList = []
        self.logs = []
        self.mapPositions = []
        self.mainCharacter = None

        self.setUpWorld()

    def setUpWorld(self):
        self.killList.clear()
        self.organisms.clear()

        if self.mainCharacter is not None:
            mainCharacter = None

        numberOfElements = int(self.mapSize.getX() * self.mapSize.getY() * 0.2)

        for i in range(numberOfElements):
            newOrganism = self.getRandomOrganism()
            self.organisms.append(newOrganism)

        mainCharacter = Human(self, 5, 5)

        for i in range(numberOfElements):
            if mainCharacter.getPosition().getX() == self.organisms[i].getPosition().getX() and mainCharacter.getPosition().getY() == self.organisms[i].getPosition().getY():
                self.organisms.pop(i)
                break

        self.organisms.append(mainCharacter)

    def getRandomOrganism(self):
        randomNumberOfOrg = random.randint(0, 9)
        # randomNumberOfOrg = 4

        if randomNumberOfOrg == 0:
            newOrganism = Antylope(self, int(random.random() * self.mapSize.getX()), int(random.random() * self.mapSize.getY()))
        elif randomNumberOfOrg == 1:
            newOrganism = Fox(self, int(random.random() * self.mapSize.getX()), int(random.random() * self.mapSize.getY()))
        elif randomNumberOfOrg == 2:
            newOrganism = Sheep(self, int(random.random() * self.mapSize.getX()), int(random.random() * self.mapSize.getY()))
        elif randomNumberOfOrg == 3:
            newOrganism = Turtle(self, int(random.random() * self.mapSize.getX()), int(random.random() * self.mapSize.getY()))
        elif randomNumberOfOrg == 4:
            newOrganism = Wolf(self, int(random.random() * self.mapSize.getX()), int(random.random() * self.mapSize.getY()))
        elif randomNumberOfOrg == 5:
            newOrganism = Belladonna(self, int(random.random() * self.mapSize.getX()), int(random.random() * self.mapSize.getY()))
        elif randomNumberOfOrg == 6:
            newOrganism = Dandelion(self, int(random.random() * self.mapSize.getX()), int(random.random() * self.mapSize.getY()))
        elif randomNumberOfOrg == 7:
            newOrganism = Grass(self, int(random.random() * self.mapSize.getX()), int(random.random() * self.mapSize.getY()))
        elif randomNumberOfOrg == 8:
            newOrganism = Guarana(self, int(random.random() * self.mapSize.getX()), int(random.random() * self.mapSize.getY()))
        else:
            newOrganism = SosnowskiBarszcz(self, int(random.random() * self.mapSize.getX()),
                                           int(random.random() * self.mapSize.getY()))

        return newOrganism

    def killOrganismsFromKillList(self):
        i = 0
        while i < len(self.killList):
            j = 0
            while j < len(self.organisms):
                if self.killList[i] == self.organisms[j]:
                    if isinstance(self.killList[i], Human):
                        mainCharacter = None
                    else:
                        self.organisms.pop(j)
                    self.killList.pop(i)
                    i -= 1
                    j -= 1
                    break
                j += 1
            i += 1

    def addNewElementToWorld(self, organism):
        self.organisms.append(organism)

    def makeActions(self, pressed):
        self.logsPointer.clear()

        numberOfOrganisms = len(self.organisms)

        for i in range(numberOfOrganisms):
            if not self.organisms[i].isDeleted():
                human = self.organisms[i] if isinstance(self.organisms[i], Human) else None
                if human is None:
                    self.organisms[i].action()
                else:
                    human.action(pressed)
                self.organisms[i].increaseAge()

        comparator = lambda first, second: -1 if first.getInitiative() > second.getInitiative() or (
                    first.getInitiative() == second.getInitiative() and first.getAge() > second.getAge()) else 1

        self.killOrganismsFromKillList()
        self.organisms.sort(comparator)

    def getOrganisms(self):
        return self.organisms

    def getAlzurStatus(self):
        return self.mainCharacter.getShieldStatus()

    def getTopBorder(self):
        return 0

    def getLeftBorder(self):
        return 0

    def getBottomBorder(self):
        return self.mapSize.getY()

    def getRightBorder(self):
        return self.mapSize.getX()

    def getHumanPosition(self):
        return self.mainCharacter.getPosition()

    def setHumanPosition(self, cords):
        self.mainCharacter.setPosition(cords)

    def addToKillList(self, deleting):
        deleting.killOrganism()
        self.killList.append(deleting)

    def getFromPosition(self, checkingCoords):
        for element in self.organisms:
            if element.getPosition().x == checkingCoords.x and element.getPosition().y == checkingCoords.y:
                return element
        return None

    def isHumanAlive(self):
        return self.mainCharacter is not None

    def getMapPosition(self):
        return self.mapPosition

    def getMapSize(self):
        return self.mapSize

    def getKillList(self):
        return self.killList

    def getLogs(self):
        return self.logsPointer

    def setMainCharacter(self, mainCharacter):
        self.mainCharacter = mainCharacter

    def addNewLog(self, log):
        self.logsPointer.append(log)









