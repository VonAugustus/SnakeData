import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Screen dimensions
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake properties
snake_block = 10
snake_speed = 15
snake_list = []
length_of_snake = 1

# Directions
x1_change = 0
y1_change = 0

# Score
score = 0

# Font
font_style = pygame.font.SysFont(None, 50)

# Initialize snake
x1 = WIDTH / 2
y1 = HEIGHT / 2

# Generate dot
def gen_dot():
    return round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0, round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

# Draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, GREEN, [x[0], x[1], snake_block, snake_block])

# Collision check
def collision_check(x, y, list):
    for segment in list[:-1]:
        if segment == (x, y):
            return True
    return False

# Main game loop
def game_loop():
    global x1_change, y1_change, x1, y1, score, length_of_snake

    running = True
    clock = pygame.time.Clock()
    dot_x, dot_y = gen_dot()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update snake position
        x1 += x1_change
        y1 += y1_change

        # Game over conditions
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0 or collision_check(x1, y1, snake_list):
            running = False

        # Drawing
        win.fill(BLACK)
        pygame.draw.rect(win, RED, [dot_x, dot_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        draw_snake(snake_block, snake_list)

        pygame.display.update()

        # Snake eating the dot
        if x1 == dot_x and y1 == dot_y:
            dot_x, dot_y = gen_dot()
            length_of_snake += 1
            score += 1

        clock.tick(snake_speed)

    # Display final score
    win.fill(BLACK)
    message = font_style.render("You Lost! Score: " + str(score), True, RED)
    win.blit(message, [WIDTH / 6, HEIGHT / 3])
    pygame.display.update()
    pygame.time.delay(3000)

    pygame.quit()

game_loop()
