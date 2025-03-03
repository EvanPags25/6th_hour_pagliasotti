import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define the colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display width and height
width = 600
height = 400

# Create the game screen
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define the snake block size and speed
block_size = 10
snake_speed = 15

# Define the font for displaying the score
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Function to display the score
def our_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    game_display.blit(value, [0, 0])


# Function to draw the snake
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], block_size, block_size])


# Function to display the message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])


# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Set the starting position of the snake
    x1 = width / 2
    y1 = height / 2

    # Set the movement speed for the snake
    x1_change = 0
    y1_change = 0

    # Initialize the snake and its length
    snake_List = []
    Length_of_snake = 1

    # Create the food at a random position
    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    clock = pygame.time.Clock()

    # Game loop
    while not game_over:

        while game_close:
            game_display.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            our_score(Length_of_snake - 1)
            pygame.display.update()

            # Check for user input to quit or restart
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event handling for user input (arrow keys)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check for snake boundary collision
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(blue)

        # Draw the food and snake
        pygame.draw.rect(game_display, yellow, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if the snake runs into itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(block_size, snake_List)
        our_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if the snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Start the game
gameLoop()
()
