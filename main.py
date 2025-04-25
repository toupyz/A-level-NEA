import pygame
from constants import *
from dungeon_generator import create_dungeon
import sys

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# -- Choose difficulty
difficulty = 'hard'  # Change to 'easy' or 'medium' or 'hard'
settings = DIFFICULTY_SETTINGS[difficulty]

# -- Generate multiple floors
FLOORS = 3
dungeons = [create_dungeon(settings['rooms'], settings['min'], settings['max']) for _ in range(FLOORS)]
current_floor = 0

# -- Find player start position
def find_start(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '<':
                return x, y
    return 1, 1

player_x, player_y = find_start(dungeons[current_floor])

def draw_grid(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            pygame.draw.rect(screen, COLORS.get(cell, (255, 0, 255)),
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def move_player(dx, dy):
    global player_x, player_y, current_floor
    new_x = player_x + dx
    new_y = player_y + dy
    tile = dungeons[current_floor][new_y][new_x]
    if tile in ['.', '<', '>']:
        player_x, player_y = new_x, new_y
        if tile == '<' and current_floor > 0:
            current_floor -= 1
            player_x, player_y = find_start(dungeons[current_floor])
        elif tile == '>' and current_floor < FLOORS - 1:
            current_floor += 1
            player_x, player_y = find_start(dungeons[current_floor])

# -- Main Loop
running = True
last_move_time = 0  # Initialize last_move_time
MOVE_DELAY = 150  # milliseconds between moves

while running:
    screen.fill((0, 0, 0))
    draw_grid(dungeons[current_floor])
    pygame.draw.rect(screen, COLORS['@'], (player_x * TILE_SIZE, player_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Floor label
    label = font.render(f'Floor {current_floor + 1}', True, (255, 255, 255))
    screen.blit(label, (10, 10))

    pygame.display.flip()

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key movement logic
    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()
    if current_time - last_move_time > MOVE_DELAY:  # Delay check for move rate
        if keys[pygame.K_w]:
            move_player(0, -1)
            last_move_time = current_time
        elif keys[pygame.K_s]:
            move_player(0, 1)
            last_move_time = current_time
        elif keys[pygame.K_a]:
            move_player(-1, 0)
            last_move_time = current_time
        elif keys[pygame.K_d]:
            move_player(1, 0)
            last_move_time = current_time

pygame.quit()
sys.exit()
