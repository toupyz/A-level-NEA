import random
from constants import WIDTH, HEIGHT

def create_dungeon(room_count, min_size, max_size):
    grid = [['#' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    rooms = []

    for _ in range(room_count):
        w, h = random.randint(min_size, max_size), random.randint(min_size, max_size)
        x, y = random.randint(1, WIDTH - w - 1), random.randint(1, HEIGHT - h - 1)
        new_room = (x, y, w, h)

        if all(not rooms_overlap(new_room, r) for r in rooms):
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
            carve_h(grid, x1, x2, y1)
            carve_v(grid, y1, y2, x2)
        else:
            carve_v(grid, y1, y2, x1)
            carve_h(grid, x1, x2, y2)

def center(room):
    x, y, w, h = room
    return (x + w // 2, y + h // 2)

def carve_h(grid, x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        grid[y][x] = '.'

def carve_v(grid, y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2) + 1):
        grid[y][x] = '.'

def add_stairs(grid, rooms):
    up = center(random.choice(rooms))
    down = center(random.choice(rooms))
    grid[up[1]][up[0]] = '<'
    grid[down[1]][down[0]] = '>'
