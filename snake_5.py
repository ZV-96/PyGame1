import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1000, 650))
game_icon = pygame.image.load('bandifruit.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake Game - by Zack van Rooyen")

# Tuples containing the colours to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 51, 51)
green = (102, 255, 178)
teal = (0, 153, 153)

# Fonts for the game
score_font = pygame.font.SysFont("comicsans", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("comicsans", 50)


def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Centre rectangle: 1000/2 = 500 and 650/2 = 325
    text_box = txt.get_rect(center=(500, 325))
    screen.blit(txt, text_box)


# Sets the speed at which the snake moves
clock = pygame.time.Clock()

quit_game = False

# Snake will be 20 x 20 pixels
snake_x = 490
snake_y = 315

snake_x_change = 0
snake_y_change = 0

# Loop to keep screen open until user presses x
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_x_change = 0
                snake_y_change = -20
            elif event.key == pygame.K_DOWN:
                snake_x_change = 0
                snake_y_change = 20

    if snake_x >= 1000 or snake_x < 0 or snake_y >= 650 or snake_y < 0:
        quit_game = True

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(black)  # Changes background to green

    # Create the snake body (rectangle)
    pygame.draw.rect(screen, teal, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    clock.tick(5)  # sets the speed which each iteration of the game
    # runs the in frames per second

message("You suck", teal, black)
pygame.display.update()
time.sleep(3)

pygame.quit()
quit()
