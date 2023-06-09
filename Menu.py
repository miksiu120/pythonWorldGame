import pygame
from Button import *
from Buttons import *
from constValues import *


class Menu:
    def __init__(self, screen):
        self.buttons = Buttons()
        self.buttons.addButton(
            Button(BUTTON_WIDTH, BUTTON_HEIGHT, WINDOW_WIDTH / 2 - BUTTON_WIDTH / 2, 200, "1.New Game", (255, 255, 255),
                   screen))
        self.buttons.addButton(
            Button(BUTTON_WIDTH, BUTTON_HEIGHT, WINDOW_WIDTH / 2 - BUTTON_WIDTH / 2, 300, "2.Load Game",
                   (255, 255, 255), screen))
        self.buttons.addButton(
            Button(BUTTON_WIDTH, BUTTON_HEIGHT, WINDOW_WIDTH / 2 - BUTTON_WIDTH / 2, 400, "3.Exit", (255, 255, 255),
                   screen))

    def drawMenu(self):
        self.buttons.drawButtons()
