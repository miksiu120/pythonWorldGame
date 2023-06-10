class Coordinates:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def equals(self, compared):
        return compared.x == self.x and compared.y == self.y

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y
