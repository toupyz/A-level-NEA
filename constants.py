TILE_SIZE = 32
WIDTH, HEIGHT = 25, 18  # In tiles
SCREEN_WIDTH = WIDTH * TILE_SIZE
SCREEN_HEIGHT = HEIGHT * TILE_SIZE

COLORS = {
    '#': (30, 30, 30),     # Wall
    '.': (200, 200, 200),  # Floor
    '<': (100, 255, 100),  # Stairs up
    '>': (255, 100, 100),  # Stairs down
    '@': (100, 100, 255),  # Player
}

DIFFICULTY_SETTINGS = {
    'easy': {'rooms': 5, 'min': 4, 'max': 6},
    'medium': {'rooms': 10, 'min': 4, 'max': 8},
    'hard': {'rooms': 16, 'min': 3, 'max': 10},
}

MOVE_DELAY = 150  # milliseconds between moves
last_move_time = 0
