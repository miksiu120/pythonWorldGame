from Animal import Animal
class Sheep(Animal):

    def __init__(self, ourWorld, posX, posY, strength = 4, initative = 4,age=0):
        self.age = age
        super().__init__(ourWorld, strength, initative, posX, posY, 'S', "Owca")

