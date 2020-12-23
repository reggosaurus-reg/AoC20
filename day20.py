TILE_SIZE = 10  # Same for both test data and real data
tiles = {}

#tiles = {2971: ["###.", "....", "#..#", ".#.."]}
while True:
    try:
        nr = int(input().split()[1][:-1])
    except:
        break
    tiles[nr] = [input() for _ in range(TILE_SIZE)]
    input()

SIZE = int(len(tiles.keys()) ** (1/2))

def show_tile(tile):
    for row in tile:
        print(row)

def rotated(img):
    """ Rotate one step clock-wise. """
    new = [["_" for _ in img] for __ in img]
    for r, row in enumerate(img):
        for c, char in enumerate(row):
            new[c][TILE_SIZE - r - 1] = char

    return ["".join(row) for row in new]

def flipped(img):
    """ Flip along the vertical axis. """
    return [row[::-1] for row in img]

def get_versions(img):
    """ All rotations/flips of an image. """
    flp = flipped(img)
    versions = [img]
    for _ in range(3):
        img = rotated(img)
        versions.append(img)
    versions.append(flp)
    for _ in range(3):
        flp = rotated(flp)
        versions.append(flp)
    return versions

def get_borders(img):
    """ Get the 4 borders of a tile. """
    return [img[0],
            img[-1],
            "".join([row[0] for row in img]),
            "".join([row[-1] for row in img])]


print("A:")

borders = {}  # border: [nr]
for nr, tile in tiles.items():
    tile_versions = get_versions(tile)
    tiles[nr] = tile_versions
    for tile in tile_versions:
        for b in get_borders(tile):
            if b not in borders:
                borders[b] = set()
            borders[b].add(nr)

domains = list(tiles.keys())  # nr:s
next_to = {nr: set() for nr in domains}
for b, nrs in borders.items():
    if len(nrs) > 1:
        x, y = nrs
        next_to[x].add(y)
        next_to[y].add(x)

result = 1
for nr, neighs in next_to.items():
    if len(neighs) == 2:
        result *= nr

print(result)


print("B:")

from copy import copy

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
UP = SIZE - 1
CORNERS = [(0, 0), (0, UP), (UP, 0), (UP, UP)]
SIDES = list(set([(0, y) for y in range(SIZE)] +
                 [(UP, y) for y in range(SIZE)] +
                 [(x, 0) for x in range(SIZE)] +
                 [(x, UP) for x in range(SIZE)])
             - set(CORNERS))


def pos_add(a, b):
    return a[0] + b[0], a[1] + b[1]

entire_image = {(x, y): [] for x in range(SIZE) for y in range(SIZE)}
variables = list(entire_image.keys())  # positions
possible = {nr: [] for nr in domains}

for nr in next_to.keys():
    n = len(next_to[nr])
    if n == 2:
        possible[nr] = CORNERS
    elif n == 3:
        possible[nr] = SIDES
    elif n == 4:
        possible[nr] = list(set(variables) - set(SIDES) - set(CORNERS))

for nr, poses in possible.items():
    for p in poses:
        entire_image[p].append(nr)

def assign(pos, nr):
    """
        Assign nr to pos and remove nr from all other pos
        and update what values are possible.
    """
    entire_image[pos] = nr
    neigh_poses = [pos_add(pos, d) for d in DIRS]
    nexts = next_to[nr]

    for npos, nrs in entire_image.items():
        # Skip already assigned
        if isinstance(nrs, int):
            continue

        # Remove the assigned nr from other poses
        if nr in nrs[:]:
            nrs.remove(nr)

        # Remove invalid neighbours
        if npos in neigh_poses:
            for n in nrs[:]:
                if n not in nexts:
                    nrs.remove(n)


# Assign top left square

assign((0, 0), entire_image[(0, 0)][0])
assign((0, 1), entire_image[(0, 1)][0])
assign((1, 0), entire_image[(1, 0)][0])
assign((1, 1), entire_image[(1, 1)][0])

# Assign rest, going by frontier
for front in range(2, SIZE):
    seq = list(range(front)) + [front] * (front + 1)
    for i in range(len(seq)):
        pos = (seq[i], seq[-(i + 1)])
        assign(pos, entire_image[pos][0])

print()
print("Entire image")
for p, nrs in entire_image.items():
    print(p, nrs)
print()
