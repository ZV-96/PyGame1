import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000, 750))
game_icon = pygame.image.load('bandifruit.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - by Zack van Rooyen")

time.sleep(5)


pygame.quit()
quit()
