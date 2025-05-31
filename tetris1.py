
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 20
COLUMNS = WIDTH // GRID_SIZE
ROWS = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SPEED = 3

# Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [2, 0, 0]] # J
]

# Tetris class
class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.grid = [[0] * COLUMNS for _ in range(ROWS)]
        self.shape = self.get_new_shape()
        self.x, self.y = COLUMNS // 2, 0
        self.score = 0

    def get_new_shape(self):
        return random.choice(SHAPES)

    def rotate_shape(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def collision(self, dx=0, dy=0):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x, new_y = self.x + x + dx, self.y + y + dy
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS or self.grid[new_y][new_x]:
                        return True
        return False

    def lock_shape(self):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.y + y][self.x + x] = 1
        self.clear_lines()
        self.shape = self.get_new_shape()
        self.x, self.y = COLUMNS // 2, 0
        if self.collision():
            self.running = False  # Game Over

    def clear_lines(self):
        new_grid = [row for row in self.grid if not all(row)]
        lines_cleared = ROWS - len(new_grid)
        self.score += lines_cleared * 100
        self.grid = [[0] * COLUMNS] * lines_cleared + new_grid

    def draw_grid(self):
        for y in range(ROWS):
            for x in range(COLUMNS):
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, WHITE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, WHITE, ((self.x + x) * GRID_SIZE, (self.y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def run(self):
        while self.running:
            self.screen.fill(BLACK)
            self.draw_grid()
            pygame.display.flip()
            self.clock.tick(SPEED)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and not self.collision(dx=-1):
                        self.x -= 1
                    elif event.key == pygame.K_RIGHT and not self.collision(dx=1):
                        self.x += 1
                    elif event.key == pygame.K_DOWN and not self.collision(dy=1):
                        self.y += 1
                    elif event.key == pygame.K_UP:
                        self.rotate_shape()
                        if self.collision():
                            self.rotate_shape()  # Undo if invalid

            if not self.collision(dy=1):
                self.y += 1
            else:
                self.lock_shape()

        print("Game Over! Score:", self.score)

# Start the game
if __name__ == "__main__":
    game = Tetris()
    game.run()
