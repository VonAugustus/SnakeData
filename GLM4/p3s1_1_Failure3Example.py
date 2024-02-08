import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_body = pygame.Surface((10, 10))
snake_body.fill((0, 255, 0))
dot_pos = [random.randint(0, WIDTH//10-1)*10, random.randint(0, HEIGHT//10-1)*10]
dot = pygame.Surface((10, 10))
dot.fill((255, 0, 0))
direction = "RIGHT"
change_to = direction
score = 0

def game_over():
    font = pygame.font.SysFont(None, 36)
    text = font.render('Game Over! Score: ' + str(score), True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()

def main():
    global direction, change_to, score
    direction = "RIGHT"
    change_to = direction
    snake_pos = [[100, 50], [90, 50], [80, 50]]
    dot_pos = [random.randint(0, WIDTH//10-1)*10, random.randint(0, HEIGHT//10-1)*10]
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"
                elif event.key == pygame.K_UP:
                    change_to = "UP"
                elif event.key == pygame.K_DOWN:
                    change_to = "DOWN"

        # Validate direction
        if change_to == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        if change_to == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"
        if change_to == "UP" and direction != "DOWN":
            direction = "UP"
        if change_to == "DOWN" and direction != "UP":
            direction = "DOWN"

        # Move snake
        if direction == "LEFT":
            snake_pos[0][0] -= 10
        if direction == "RIGHT":
            snake_pos[0][0] += 10
        if direction == "UP":
            snake_pos[0][1] -= 10
        if direction == "DOWN":
            snake_pos[0][1] += 10

        # Snake body growing mechanism
        snake_pos.insert(0, list(snake_pos[0]))
        if snake_pos[0] == dot_pos:
            dot_pos = [random.randint(0, WIDTH//10-1)*10, random.randint(0, HEIGHT//10-1)*10]
            score += 1
        else:
            snake_pos.pop()

        # Graphics
        screen.fill((0, 0, 0))
        for pos in snake_pos:
            screen.blit(snake_body, pos)
        screen.blit(dot, dot_pos)
        pygame.display.flip()

        # Game Over conditions
        if snake_pos[0][0] < 0 or snake_pos[0][0] > WIDTH-10:
            game_over()
        if snake_pos[0][1] < 0 or snake_pos[0][1] > HEIGHT-10:
            game_over()
        for block in snake_pos[1:]:
            if snake_pos[0] == block:
                game_over()

        # Refresh rate
        clock.tick(10)

if __name__ == "__main__":
    main()
