import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Game window dimensions
WIDTH, HEIGHT = 600, 400
GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Snake properties
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# FPS controller
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * SNAKE_BLOCK)) % WIDTH), (cur[1] + (y * SNAKE_BLOCK)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], SNAKE_BLOCK, SNAKE_BLOCK))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.turn((1, 0))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, WIDTH - SNAKE_BLOCK) // 10 * 10, random.randint(0, HEIGHT - SNAKE_BLOCK) // 10 * 10)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], SNAKE_BLOCK, SNAKE_BLOCK))

def drawGrid(surface):
    for y in range(0, int(HEIGHT / SNAKE_BLOCK)):
        for x in range(0, int(WIDTH / SNAKE_BLOCK)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * SNAKE_BLOCK, y * SNAKE_BLOCK), (SNAKE_BLOCK, SNAKE_BLOCK))
                pygame.draw.rect(surface, WHITE, r)
            else:
                rr = pygame.Rect((x * SNAKE_BLOCK, y * SNAKE_BLOCK), (SNAKE_BLOCK, SNAKE_BLOCK))
                pygame.draw.rect(surface, BLACK, rr)

def main():
    snake = Snake()
    food = Food()

    while True:
        snake.handle_keys()
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        GAME_WINDOW.fill((0, 0, 0))
        drawGrid(GAME_WINDOW)
        snake.draw(GAME_WINDOW)
        food.draw(GAME_WINDOW)
        pygame.display.update()
        clock.tick(SNAKE_SPEED)

main()
