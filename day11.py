from copy import deepcopy

DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
seats = []
while True:
    try:
        row = input()
    except:
        break
    seats.append(list(row))

H = len(seats)
W = len(seats[0])
seatsB = deepcopy(seats)


print("A: ")

def num_occupied(x, y):
    res = 0
    for d in DIRS:
        new_x = x + d[0]
        new_y = y + d[1]
        if 0 <= new_x < W and 0 <= new_y < H:
            if seats[new_y][new_x] == "#":
                res += 1
    return res

while True:
    new_seats = deepcopy(seats)
    changed = False
    for y in range(H):
        for x in range(W):
            if seats[y][x] == "L" and num_occupied(x, y) == 0:
                new_seats[y][x] = "#"
                changed = True
            elif seats[y][x] == "#" and num_occupied(x, y) >= 4:
                new_seats[y][x] = "L"
                changed = True
            else:
                new_seats[y][x] = seats[y][x]
    if not changed:
        break
    seats = deepcopy(new_seats)

print(sum(row.count("#") for row in seats))


print("B: ") # (Same as A but different num_occupied and 5 instead of 4...)

seats = deepcopy(seatsB)
def num_occupied_B(x, y):
    res = 0
    for d in DIRS:
        new_x = x + d[0]
        new_y = y + d[1]
        while 0 <= new_x < W and 0 <= new_y < H:
            if seats[new_y][new_x] == "#":
                res += 1
                break
            if seats[new_y][new_x] == "L":
                break
            else:
                new_x += d[0]
                new_y += d[1]
    return res

while True:
    new_seats = deepcopy(seats)
    changed = False
    for y in range(H):
        for x in range(W):
            if seats[y][x] == "L" and num_occupied_B(x, y) == 0:
                new_seats[y][x] = "#"
                changed = True
            elif seats[y][x] == "#" and num_occupied_B(x, y) >= 5:
                new_seats[y][x] = "L"
                changed = True
            else:
                new_seats[y][x] = seats[y][x]
    if not changed:
        break
    seats = deepcopy(new_seats)

print(sum(row.count("#") for row in seats))
