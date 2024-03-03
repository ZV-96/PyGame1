import pygame
import time
import random
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

clock = pygame.time.Clock()


# Function to track highscore
def load_high_score():
    try:
        high_score_file = open("highscore.txt", 'r')
    except IOError:
        high_score_file = open("highscore.txt", 'w')
        high_score_file.write("0")
    high_score_file_score_file = open("highscore.txt", 'r')
    value = high_score_file.read()
    high_score_file.close()
    return value


def update_high_score(score, high_score):
    if int(score) > int(high_score):
        return score
    else:
        return high_score


# update high score
def save_high_score(high_score):
    high_score_file = open("highscore.txt", 'w')
    high_score_file.write(str(high_score))
    high_score_file.close()


# Display player score
def user_score(score, score_colour, high_score):
    display_score = score_font.render(f"Score: {score}", True, score_colour)
    screen.blit(display_score, (800, 20))  # Coordinates for top right

    # High_score
    display_score = score_font.render(f"High Score: {high_score}", True,
                                      score_colour)
    screen.blit(display_score, (20, 20))


# create snake
def draw_snake(snake_list):
    print(f"Snake list: {snake_list}")  # for debugging
    for i in snake_list:
        pygame.draw.rect(screen, teal, [i[0], i[1], 20, 20])


# Function to display message on screen
def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Center rectangle: 1000/2 = 500, 720/2 = 360
    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)


# main game loop
def game_loop():
    start_time = time.time()
    quit_game = False
    game_over = False

    # snake will be 20x20 pixels
    snake_x = 480   # Centre point horizontally is (1000-20)-20 = 480
    snake_y = 340   # Centre point vertically is (720-2)/2 = 350

    snake_x_change = 0  # holds the value of changes in the x-coordinate
    snake_y_change = 0  # holds the value of changes in the y-coordinate
    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 720 - 20) / 20) * 20

    # Load the high score
    high_score = load_high_score()
    print(f"high_score test: {high_score}")  # for debugging

    while not quit_game:
        # gives user the option to quit or play again when they die
        while game_over:
            save_high_score(high_score)
            screen.fill(white)
            message("Press 'Q' or Quit or 'A' to play again", black, white)
            pygame.display.update()

            # Check if user wants to quit or play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()  # restart the main game loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = "Exit: X to Quit or R to reset"
                message(instructions, white, black)
                pygame.display.update()

                end = False
                while not end:
                    for event in pygame.event.get():
                        # if user presses x button, game quits.
                        if event.type == pygame.QUIT:
                            end = True
                            game_over = True

                    # if user presses 'R' button again, game is reset
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            end = True, game_loop()

                        # If user presses 'Q' button, game quits
                    if event.key == pygame.K_q:
                        quit_game = True
                        end = True

            # Original set-up for arrow keys to move the snake
            # Handling snake movement
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

        if snake_x >= 1000 or snake_x < 0 or snake_y >= 720 or snake_y < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(white)  # changes screen to white

        # create rectangle for snake
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        draw_snake(snake_list)

        # Keeping track of the player's score
        score = snake_length - 1
        user_score(score, black, high_score)

        #  Get high score
        high_score = update_high_score(score, high_score)

        # Link speed of snake to player score to increase difficulty
        if score > 3:
            speed = score
        else:
            speed = 3

        # create circle for food
        food = pygame.Rect(food_x, food_y, 20, 20)
        apple = pygame.image.load('bandifruit.png').convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20, 20])
        screen.blit(resized_apple, food)

        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            # Set new random position for food in snake touches it
            food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
            food_y = round(random.randrange(20, 720 - 20) / 20) * 20

            # Increase length of snake (by original size)
            snake_length += 1

        clock.tick(speed)  # 5 frames per second

    pygame.quit()
    quit()


# Main routine
game_loop()
