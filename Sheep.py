from Animal import Animal
class Sheep(Animal):
    def __init__(self, ourWorld, posX, posY):
        super().__init__(ourWorld, 4, 4, posX, posY, 'S', "Owca")

    def __init__(self, ourWorld, posX, posY, strength = 4, initative = 4):
        super().__init__(ourWorld, strength, initative, posX, posY, 'S', "Owca")

