import pygame
pygame.init()
class Button:
    def __init__(self, width, height, x, y, text, color, screen):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        text = pygame.font.SysFont("Arial.ttf", 30).render(self.text, True, (0, 0, 0))
        self.screen.blit(text, (self.x + 10, self.y + 10))