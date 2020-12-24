from copy import copy

floor = {(0, 0): False}  # Pos: color where False = white, True = black
REF = (0, 0)
DIRS = {
        "e":  (2, 0),
        "se": (1, 1),
        "sw": (-1, 1),
        "w":  (-2, 0),
        "nw": (-1, -1),
        "ne": (1, -1),
        }

def tup_add(a, b):
    return a[0] + b[0], a[1] + b[1]


print("A:")

def color(steps):
    pos = REF
    for s in steps:
        pos = tup_add(pos, DIRS[s])

    if pos not in floor:
        floor[pos] = False

    floor[pos] = not floor[pos]

while True:
    try:
        row = input()
    except:
        break

    seq = []
    step = ""
    for c in row:
        if c in "we":
            step += c
            seq.append(step)
            step = ""
        elif c in "ns":
            step += c

    color(seq)

print(sum(floor.values()))


print("B:")


def get_neighbous(pos):
    return [tup_add(pos, d) for d in DIRS.values()]

def num_black_neighbours(pos):
    return sum([floor.get(n, False) for n in get_neighbous(pos)])


DAYS = 100
for _ in range(DAYS):
    extended_floor = copy(floor)

    # Extend floor by 1 in each direction
    for tile in floor.keys():
        for neigh in get_neighbous(tile):
            if neigh in floor:
                extended_floor[neigh] = floor[neigh]
            else:
                extended_floor[neigh] = False

    # Flip
    new_floor = {}
    for tile in extended_floor.keys():
        num = num_black_neighbours(tile)
        if extended_floor[tile] and num == 0 or num > 2:
            new_floor[tile] = False
        elif not extended_floor[tile] and num == 2:
            new_floor[tile] = True
        else:
            new_floor[tile] = extended_floor[tile]

    floor = copy(new_floor)
    # print(f"Day {_+1}: {sum(floor.values())}") # For progress. ;)

print(sum(floor.values()))
