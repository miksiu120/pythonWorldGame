from Animal import Animal
from Coordinates import Coordinates

class Human(Animal):

    def __init__(self, ourWorld, posX, posY, strength = 5, initative = 4, alzurShieldCooldown = 0):
        super().__init__(ourWorld, strength, initative, posX, posY, '7', "Czlowiek")
        self.alzurShieldCooldown = alzurShieldCooldown
        self.isShieldActive = False

    def action(self, ascii):
        if self.alzurShieldCooldown > 0:
            self.alzurShieldCooldown -= 1

        if ascii == 'a' and self.canMove(Coordinates(self.getX() - 1, self.getY())):
            potential = self.ourWorld.getFromPosition(Coordinates(self.getX() - 1, self.getY()))
            self.ourWorld.addNewLog("Czlowiek idzie na pole (" + str(self.getX() - 1) + " " + str(self.getY()) + ")")
            self.collision(potential)
            self.setX(self.getX() - 1)
        elif ascii == 'w' and self.canMove(Coordinates(self.getX(), self.getY() - 1)):
            potential = self.ourWorld.getFromPosition(Coordinates(self.getX(), self.getY() - 1))
            self.ourWorld.addNewLog("Czlowiek idzie na pole (" + str(self.getX()) + " " + str(self.getY() - 1) + ")")
            self.collision(potential)
            self.setY(self.getY() - 1)
        elif ascii == 's' and self.canMove(Coordinates(self.getX(), self.getY() + 1)):
            potential = self.ourWorld.getFromPosition(Coordinates(self.getX(), self.getY() + 1))
            self.ourWorld.addNewLog("Czlowiek idzie na pole (" + str(self.getX()) + " " + str(self.getY() + 1) + ")")
            self.collision(potential)
            self.setY(self.getY() + 1)
        elif ascii == 'd' and self.canMove(Coordinates(self.getX() + 1, self.getY())):
            potential = self.ourWorld.getFromPosition(Coordinates(self.getX() + 1, self.getY()))
            self.ourWorld.addNewLog("Czlowiek idzie na pole (" + str(self.getX() + 1) + " " + str(self.getY()) + ")")
            self.collision(potential)
            self.setX(self.getX() + 1)

        if self.alzurShieldCooldown == 5:
            self.isShieldActive = False

        if ascii == 'g' and self.alzurShieldCooldown == 0:
            self.alzurShieldCooldown = 10
            self.isShieldActive = True
            self.ourWorld.addNewLog("Czlowiek aktywuje tarcze Alzura")

    def collision(self, attacker):
        if attacker is None or self is None:
            return

        animal = attacker if isinstance(attacker, Animal) else None

        if self.isShieldActive == False:
            super().collision(attacker)
        elif animal is not None:
            newCoords = self.getEmptyNeighbour()

            if newCoords.getX() != -1 and newCoords.getY() != -1:
                attacker.setPosition(newCoords)

    def getShieldStatus(self):
        return self.isShieldActive

    def getShieldCooldown(self):
        return self.alzurShieldCooldown

    def setShieldStatus(self, status):
        self.isShieldActive = status

    def setShieldCooldown(self, cooldown):
        self.alzurShieldCooldown = cooldown