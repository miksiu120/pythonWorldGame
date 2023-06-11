# I have to change the of the file to GameWindow.py, but I don't have any idea yet

from graphicFiles.Square import *
from graphicFiles.constValues import *
from World import *
from Logs import *
class GameWindow:
    def __init__(self, blocksWidth, blocksHeight, screen):
        self.blocksWidth = blocksWidth
        self.blocksHeight = blocksHeight
        self.screen = screen
        self.squares = []
        self.world = World(self.blocksWidth, self.blocksHeight)
        self.logPanel = LogPanel(self.world.getLogs())
        for i in range(self.blocksWidth):
            self.squares.append([])
            for j in range(self.blocksHeight):
                asciiToShow = None
                if self.world.getFromPosition(Coordinates(j,i)) == None:
                    asciiToShow = ""
                else:
                    asciiToShow = self.world.getFromPosition(Coordinates(j,i)).getAscii()

                self.squares[i].append(Square(BLOCK_WIDTH, BLOCK_HEIGHT, asciiToShow, (100 + 100 * ((j+i) % 2), 100 + 100 * ((j+i) % 2), 100 + 100 * ((j+i) % 2)), i * BLOCK_WIDTH, j * BLOCK_HEIGHT))
        self.updateSquares()


    def updateSquares(self):
        for i in range(self.blocksHeight):
            for j in range(self.blocksWidth):
                self.squares[i][j].setAscii("")

        for i in range(len(self.world.getOrganisms())):
            self.squares[self.world.getOrganisms()[i].getX()][self.world.getOrganisms()[i].getY()].setAscii(self.world.getOrganisms()[i].getName())



    def draw(self):
        for i in range(self.blocksWidth):
            for j in range(self.blocksHeight):
                self.squares[i][j].draw(self.screen)

    def movePlayer(self, direction):
        self.world.makeActions(direction)
        self.updateSquares()
        self.logPanel.writeLogs()