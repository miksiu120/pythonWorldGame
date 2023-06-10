from Animal import Animal


class Wolf(Animal):


    def __init__(self, ourWorld, posX, posY, strength = 9, initative = 5, age = 0):
        super().__init__(ourWorld, strength, initative, posX, posY, 'W', "Wilk")
