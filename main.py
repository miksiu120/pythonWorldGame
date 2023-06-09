import pygame
from Game import *

pygame.init()
newGame = Game(WINDOW_WIDTH, WINDOW_HEIGHT, "rzycie")
newGame.playGame()

# # Inicjalizacja biblioteki Pygame
# pygame.init()
#
# # Ustalenie szerokości i wysokości planszy
# width = 800
# height = 600
#
# # Utworzenie planszy gry
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Prosta gra planszowa")
#
# # Ustalenie początkowej pozycji gracza
# player_x = 50
# player_y = 50
#
# # Główna pętla gry
# running = True
# while running:
#     # Obsługa zdarzeń
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             # Poruszanie gracza za pomocą strzałek
#             if event.key == pygame.K_LEFT:
#                 player_x -= 50
#             elif event.key == pygame.K_RIGHT:
#                 player_x += 50
#             elif event.key == pygame.K_UP:
#                 player_y -= 50
#             elif event.key == pygame.K_DOWN:
#                 player_y += 50
#
#     # Wyczyszczenie planszy
#     screen.fill((0, 0, 0))
#
#     # Narysowanie gracza na planszy
#     pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, 50, 50))
#
#     # Zaktualizowanie planszy
#     pygame.display.flip()
#
# # Zakończenie gry
# pygame.quit()
