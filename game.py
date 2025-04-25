#import pygame
#pygame.init()
#screen = pygame.display.set_mode((750, 700))
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#pygame.quit()

import random

def create_dungeon(width, height, room_count, min_size, max_size):
    grid = [['#' for _ in range(width)] for _ in range(height)]
    rooms = []

    for _ in range(room_count):
        w, h = random.randint(min_size, max_size), random.randint(min_size, max_size)
        x, y = random.randint(1, width - w - 1), random.randint(1, height - h - 1)
        new_room = (x, y, w, h)

        if all(not rooms_overlap(new_room, room) for room in rooms):
            rooms.append(new_room)
            carve_room(grid, new_room)

    connect_rooms(grid, rooms)
    add_stairs(grid, rooms)
    return grid

def rooms_overlap(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return (ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by)

def carve_room(grid, room):
    x, y, w, h = room
    for i in range(x, x + w):
        for j in range(y, y + h):
            grid[j][i] = '.'

def connect_rooms(grid, rooms):
    for i in range(1, len(rooms)):
        x1, y1 = center(rooms[i - 1])
        x2, y2 = center(rooms[i])
        if random.choice([True, False]):
            carve_h_corridor(grid, x1, x2, y1)
            carve_v_corridor(grid, y1, y2, x2)
        else:
            carve_v_corridor(grid, y1, y2, x1)
            carve_h_corridor(grid, x1, x2, y2)

def center(room):
    x, y, w, h = room
    return (x + w // 2, y + h // 2)

def carve_h_corridor(grid, x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        grid[y][x] = '.'

def carve_v_corridor(grid, y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2) + 1):
        grid[y][x] = '.'

def add_stairs(grid, rooms):
    up_room = random.choice(rooms)
    down_room = random.choice([r for r in rooms if r != up_room])
    ux, uy = center(up_room)
    dx, dy = center(down_room)
    grid[uy][ux] = '<'
    grid[dy][dx] = '>'

def print_dungeon(grid):
    for row in grid:
        print(''.join(row))

# Example usage
dungeon = create_dungeon(40, 25, room_count=10, min_size=4, max_size=8)
print_dungeon(dungeon)
