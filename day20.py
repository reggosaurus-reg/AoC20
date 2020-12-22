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

#t = tiles[2971]
#for i in get_versions(t):
#    print()
#    show_tile(i)

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
        print(nr)
        result *= nr

print(result)

#constraints = {nr: [] for nr in domains} # next to other nr:s

#for nr in domains:
#    for border in tiles[nr]:


final_image = {(x, y): None for x in range(SIZE) for y in range(SIZE)}
variables = list(final_image.keys())  # positions

def first_free(img):
    for v in variables:
        if img[v] is None:
            return v
    return False

to_assign = list(tiles.keys())

#print(variables)
