from Animal import Animal
from Coordinates import Coordinates
class CyberSheep(Animal):
    def __init__(self, ourWorld, posX, posY, strength = 15, initative = 4,age=0):
        self.age = age
        super().__init__(ourWorld, strength, initative, posX, posY, 'C', "Cyber")


    def getClosestNeighbourFromBarszcz(self,closestBarszczCords):
        neighboursCords = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        distanceFromSheep = abs(self.getPosition().getX() - closestBarszczCords.getX()) + abs(self.getPosition().getY() - closestBarszczCords.getY())
        for neighbourCords in neighboursCords:
            distanceFromNeighbour = abs(self.getPosition().getX() + neighbourCords[0] - closestBarszczCords.getX()) + abs(self.getPosition().getY() + neighbourCords[1] - closestBarszczCords.getY())
            if(distanceFromNeighbour < distanceFromSheep):
                return neighbourCords
    def action(self):
        if self.ourWorld.isBarszczOnBoard():
            closestBarszczCords = self.ourWorld.getClosestBarszczCords(self)
            print("Najblizszy barszcz:" + str(closestBarszczCords.getX()) + " " + str(closestBarszczCords.getY()))
            closestNeighour = self.getClosestNeighbourFromBarszcz(closestBarszczCords)
            print("Najblizszy sasiad:" + str(closestNeighour[0]) + " " + str(closestNeighour[1]))
            super().action(Coordinates(closestNeighour[0], closestNeighour[1]))
        else:
            super().action()
