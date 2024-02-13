"""Snake_2 but replacing timer with a
time loop to prevent game from
closing unless 'X' is clicked"""

import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 750))
game_icon = pygame.image.load('bandifruit.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - by Zack van Rooyen")

quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

pygame.quit()
quit()
