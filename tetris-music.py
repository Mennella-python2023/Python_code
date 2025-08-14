
import pygame
import random
import time

# Inizializza Pygame e il mixer audio
pygame.init()
pygame.mixer.init()

# Costanti
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 25
COLUMNS = WIDTH // GRID_SIZE
ROWS = HEIGHT // GRID_SIZE
SPEED = 3
BLACK = (0, 0, 0)


# Forme e colori dei pezzi
SHAPES = [
    ([[1, 1, 1, 1]], (0, 255, 255)),  # I - Cyan
    ([[1, 1], [1, 1]], (225, 225, 0)),  # O - Yellow
    ([[1, 1, 1], [0, 1, 0]], (128, 0, 128)),  # T - Purple 
    ([[1, 1, 0], [0, 1, 1]], (0, 255, 0)),  # S - Green
    ([[0, 1, 1], [1, 1, 0]], (255, 0, 0)),  # Z - Red
    ([[1, 1, 1], [1, 0, 0]], (255, 165, 0)),  # L - Orange
    ([[1, 1, 1], [0, 0, 1]], (0, 0, 255))  # J - Blue
    
]

# Classe Tetris
class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.grid = [[(0, 0, 0)] * COLUMNS for _ in range(ROWS)]
        self.shape, self.color = self.get_new_shape()
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
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS or self.grid[new_y][new_x] != (0, 0, 0):
                        return True
        return False

    def lock_shape(self):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.y + y][self.x + x] = self.color
        self.animate_clear_lines()
        self.shape, self.color = self.get_new_shape()
        self.x, self.y = COLUMNS // 2, 0
        if self.collision():
            self.running = False  # Game Over

    def animate_clear_lines(self):
        """Animazione di dissolvenza quando una riga viene eliminata"""
        full_rows = [y for y in range(ROWS) if all(self.grid[y][x] != (0, 0, 0) for x in range(COLUMNS))]
        if full_rows:
            for step in range(3):  # Dissolvenza in 3 passaggi
                for y in full_rows:
                    for x in range(COLUMNS):
                        r, g, b = self.grid[y][x]
                        self.grid[y][x] = (r//2, g//2, b//2)  # Diminuisce la luminosità
                self.draw_grid()
                pygame.display.flip()
                time.sleep(0.3)  # Piccola pausa tra gli step

            # Rimuove le righe dopo l'animazione
            self.grid = [[(0, 0, 0)] * COLUMNS] * len(full_rows) + [row for row in self.grid if row not in [self.grid[y] for y in full_rows]]
            self.score += len(full_rows) * 100

    def draw_grid(self):
        for y in range(ROWS):
            for x in range(COLUMNS):
                if self.grid[y][x] != (0, 0, 0):
                    pygame.draw.rect(self.screen, self.grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, self.color, ((self.x + x) * GRID_SIZE, (self.y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))

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
                            self.rotate_shape()  # Annulla se invalida

            if not self.collision(dy=1):
                self.y += 1
            else:
                self.lock_shape()

        print("Game Over! Score:", self.score)

# Avvia il gioco
if __name__ == "__main__":
    game = Tetris()
    game.run()
