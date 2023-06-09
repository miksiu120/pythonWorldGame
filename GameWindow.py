# I have to change the of the file to GameWindow.py, but I don't have any idea yet
from constValues import *

from Square import *
from constValues import *
class GameWindow:
    def __init__(self, blocksWidth, blocksHeight, screen):
        self.blocksWidth = blocksWidth
        self.blocksHeight = blocksHeight
        self.screen = screen
        self.squares = []
        for i in range(self.blocksWidth):
            self.squares.append([])
            for j in range(self.blocksHeight):
                self.squares[i].append(Square(BLOCK_WIDTH, BLOCK_HEIGHT, "Kupa", (100 + 100 * ((j+i) % 2), 100 + 100 * ((j+i) % 2), 100 + 100 * ((j+i) % 2)), i * BLOCK_WIDTH, j * BLOCK_HEIGHT))



    def draw(self):
        for i in range(self.blocksWidth):
            for j in range(self.blocksHeight):
                self.squares[i][j].draw(self.screen)
