import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
PLAYER_SPEED = 5
OBSTACLE_SIZE = 40
PLAYER_SIZE = 40
WORLD_SIZE = 2000  # Simulating a larger world

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Open-World Game")

# Fonts
font = pygame.font.SysFont("Arial", 24)

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = PLAYER_SPEED

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Prevent the player from going out of bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Obstacle Class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_SIZE, OBSTACLE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Set up sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Create the player
player = Player()
all_sprites.add(player)

# Create random obstacles in the world
for _ in range(10):  # 10 obstacles
    x = random.randint(0, SCREEN_WIDTH - OBSTACLE_SIZE)
    y = random.randint(0, SCREEN_HEIGHT - OBSTACLE_SIZE)
    obstacle = Obstacle(x, y)
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Game Loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Check for collisions with obstacles
    if pygame.sprite.spritecollide(player, obstacles, False):
        player.rect.x -= PLAYER_SPEED  # Prevent player from moving into obstacles

    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Display player position
    position_text = font.render(f"Position: ({player.rect.x}, {player.rect.y})", True, WHITE)
    screen.blit(position_text, (10, 10))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
