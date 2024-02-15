"""Snake_2 but replacing timer with a
time loop to prevent game from
closing unless 'X' is clicked and
 adding colors/fonts"""

import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 750))
game_icon = pygame.image.load('bandifruit.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - by Zack van Rooyen")

# Tuples containing the colors to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (188, 227, 199)

# Fonts for Game
score_font = pygame.font.SysFont("comicsans", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)

quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

pygame.quit()
quit()
