from graphicFiles.Menu import *
from graphicFiles.GameWindow import *
from graphicFiles.constValues import *


class Game:
    def __init__(self, width, height, caption):
        self.caption = caption
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True

        pygame.display.set_caption(self.caption)

        self.gameMenu = Menu(self.screen)
        self.gameWindow = GameWindow(20, 20, self.screen)

        self.handlerType = "menu"


    def createNewGame(self):
        self.handlerType = "game"
        self.gameWindow = GameWindow(15, 15, self.screen)
        screen = pygame.display.set_mode((15 * BLOCK_WIDTH, 15 * BLOCK_HEIGHT))

    def draw(self):
        self.screen.fill((21, 37, 69))
        if self.handlerType == "menu":
            self.gameMenu.drawMenu()
        elif self.handlerType == "game":
            self.gameWindow.draw()
        pygame.display.flip()

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.handlerType == "menu":
                    if event.key == pygame.K_1:
                        print("1")
                        self.createNewGame()
                        self.handlerType = "game"
                    elif event.key == pygame.K_2:
                        print("2")
                        self.handlerType = "game"
                    elif event.key == pygame.K_3:
                        self.running = False
                elif self.handlerType == "game":
                    if event.key == pygame.K_w:
                        print ("w")
                        self.gameWindow.movePlayer('w')
                    elif event.key == pygame.K_s:
                        self.gameWindow.movePlayer('s')
                    elif event.key == pygame.K_a:
                        self.gameWindow.movePlayer('a')
                    elif event.key == pygame.K_d:
                        self.gameWindow.movePlayer('d')

    def playGame(self):
        while self.running:
            self.draw()
            self.eventHandler()
