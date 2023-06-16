from Plant import Plant
class Belladonna(Plant):

    def __init__(self, ourWorld, posX, posY, strength=99, initative=0,age=0):
        self.age = age
        super().__init__(ourWorld, strength, initative, posX, posY,'B', 5,"Wilcza jagoda")
