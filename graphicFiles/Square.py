
import pygame

class Square:
    def __init__(self, width, height, organismToShow, color, posX, posY):
        self.width = width
        self.height = height
        self.organismToShow = organismToShow
        self.color = color
        self.posX = posX
        self.posY = posY

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.posX, self.posY, self.width, self.height))
        text = pygame.font.SysFont("Arial.ttf", 20).render(self.organismToShow, True, (0, 0, 0))
        screen.blit(text, (self.posX, self.posY))

    def setAscii(self, ascii):
        self.organismToShow = ascii



