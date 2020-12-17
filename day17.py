from copy import deepcopy

CYCLES = 6

grid = {}
gridB = {}
y = 0
while True:
    try:
        row = input()
    except:
        break
    for x, status in enumerate(row):
        grid[(x, y, 0)] = status
        gridB[(x, y, 0, 0)] = status
    y += 1

def get_new_cell(num_active, cell):
    if cell == "#":
        if num_active in [2, 3]:
            return "#"
        else:
            return "."
    if cell == ".":
        if num_active == 3:
            return "#"
        else:
            return "."

print("A: ")

def print_grid(grid):
    k = grid.keys()
    min_x = min(map(lambda d: d[0], k))
    min_y = min(map(lambda d: d[1], k))
    min_z = min(map(lambda d: d[2], k))
    max_x = max(map(lambda d: d[0], k)) + 1
    max_y = max(map(lambda d: d[1], k)) + 1
    max_z = max(map(lambda d: d[2], k)) + 1

    for z in range(min_z, max_z):
        print()
        print(f"z = {z}")
        g = sorted(grid, key=lambda d: d[1])
        for y in range(min_y, max_y):
            for pos in g:
                if pos[1] == y and pos[2] == z:
                    print(grid[pos], end="")
            print()

def get_relevant_cells(k):
    min_x = min(map(lambda d: d[0], k)) - 1
    min_y = min(map(lambda d: d[1], k)) - 1
    min_z = min(map(lambda d: d[2], k)) - 1
    max_x = max(map(lambda d: d[0], k)) + 2
    max_y = max(map(lambda d: d[1], k)) + 2
    max_z = max(map(lambda d: d[2], k)) + 2

    cells = []
    for z in range(min_z, max_z):
        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                pos = (x, y, z)
                cells.append(pos)
    return cells

def get_neighbours(pos):
    neighbours = []
    x, y, z = pos
    for new_x in range(x-1, x+2):
        for new_y in range(y-1, y+2):
            for new_z in range(z-1, z+2):
                new_pos = (new_x, new_y, new_z)
                neighbours.append(new_pos)
    neighbours.remove(pos)
    return neighbours

def get_active(grid, neighbours):
    active = 0
    for n in neighbours:
        if not n in grid:
            continue
        active += (grid[n] == "#")
    return active

for _ in range(CYCLES):
    new_grid = {}
    for pos in get_relevant_cells(grid.keys()):
        cell = grid.get(pos, ".")
        neighbours = get_neighbours(pos)
        num_active = get_active(grid, neighbours)
        new_grid[pos] = get_new_cell(num_active, cell)

    grid = deepcopy(new_grid)

print(sum(map(lambda c: c == "#", grid.values())))


print("B: ")

def print_grid(grid):
    k = grid.keys()
    min_x = min(map(lambda d: d[0], k))
    min_y = min(map(lambda d: d[1], k))
    min_z = min(map(lambda d: d[2], k))
    min_w = min(map(lambda d: d[3], k))

    max_x = max(map(lambda d: d[0], k)) + 1
    max_y = max(map(lambda d: d[1], k)) + 1
    max_z = max(map(lambda d: d[2], k)) + 1
    max_w = max(map(lambda d: d[3], k)) + 1

    print(list(range(min_z, max_z)))
    print(list(range(min_w, max_w)))
    for w in range(min_w, max_w):
        for z in range(min_z, max_z):
            print()
            print(f"z = {z}, w = {w}")
            g = sorted(grid, key=lambda d: d[1])
            for y in range(min_y, max_y):
                for pos in g:
                    if pos[1] == y and pos[2] == z and pos[3] == w:
                        print(grid[pos], end="")
                print()

def get_relevant_cells(k):
    min_x = min(map(lambda d: d[0], k)) - 1
    min_y = min(map(lambda d: d[1], k)) - 1
    min_z = min(map(lambda d: d[2], k)) - 1
    min_w = min(map(lambda d: d[3], k)) - 1

    max_x = max(map(lambda d: d[0], k)) + 2
    max_y = max(map(lambda d: d[1], k)) + 2
    max_z = max(map(lambda d: d[2], k)) + 2
    max_w = max(map(lambda d: d[3], k)) + 2

    cells = []
    for w in range(min_w, max_w):
        for z in range(min_z, max_z):
            for y in range(min_y, max_y):
                for x in range(min_x, max_x):
                    pos = (x, y, z, w)
                    cells.append(pos)
    return cells

def get_neighbours(pos):
    neighbours = []
    x, y, z, w = pos
    for new_x in range(x-1, x+2):
        for new_y in range(y-1, y+2):
            for new_z in range(z-1, z+2):
                for new_w in range(w-1, w+2):
                    new_pos = (new_x, new_y, new_z, new_w)
                    neighbours.append(new_pos)
    neighbours.remove(pos)
    return neighbours

grid = deepcopy(gridB)
for _ in range(CYCLES):
    new_grid = {}
    for pos in get_relevant_cells(grid.keys()):
        cell = grid.get(pos, ".")
        neighbours = get_neighbours(pos)
        num_active = get_active(grid, neighbours)
        new_grid[pos] = get_new_cell(num_active, cell)

    grid = deepcopy(new_grid)

print(sum(map(lambda c: c == "#", grid.values())))

