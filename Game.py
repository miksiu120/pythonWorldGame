import pygame
from Button import Button
from Buttons import Buttons

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

class Game:
    def __init__(self, width, height, caption):
        self.caption = caption
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        pygame.display.set_caption(self.caption)
        self.buttons = Buttons()
        self.buttons.add_button(Button(BUTTON_WIDTH, BUTTON_HEIGHT, WINDOW_WIDTH/2 - BUTTON_WIDTH/2, 200, "1.New Game", (255, 255, 255), self.screen))
        self.buttons.add_button(Button(BUTTON_WIDTH, BUTTON_HEIGHT, WINDOW_WIDTH/2 - BUTTON_WIDTH/2, 300, "2.Load Game", (255, 255, 255), self.screen))
        self.buttons.add_button(Button(BUTTON_WIDTH, BUTTON_HEIGHT, WINDOW_WIDTH/2 - BUTTON_WIDTH/2, 400, "3.Exit", (255, 255, 255), self.screen))
        self.handlerType = "menu"
    def draw(self):
        self.screen.fill((21, 37, 69))
        self.buttons.drawButtons()
        pygame.display.flip()
    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.handlerType == "menu":
                    if event.key == pygame.K_1:
                        print("1")
                    elif event.key == pygame.K_2:
                        print("2")
                    elif event.key == pygame.K_3:
                        self.running = False


    def playGame(self):
        while self.running:
            self.draw()
            self.eventHandler()




