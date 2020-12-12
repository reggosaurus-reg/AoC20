from math import sin, cos, radians

DIRS = {"N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0)
        }


TURNS = ["E", "S", "W", "N"]

def add(x, y):
    return x[0] + y[0], x[1] + y[1]

def sub(x, y):
    return x[0] - y[0], x[1] - y[1]

def mult(x, n):
    return x[0] * n, x[1] * n

def dir_to_move(angle):
    angle = radians(angle)
    x = round(sin(angle), 3)
    y = round(cos(angle), 3)
    return x, -y

actions = []
while True:
    try:
        row = input()
    except:
        break

    a = row[0]
    n = int(row[1:])
    actions.append((a, n))

print("A: ")

pos = (0, 0)
ang = 90

for a, n in actions:
    if a == "R":
        ang += n
        ang %= 360
    if a == "L":
        ang -= n
        ang %= 360

    if a == "F":
        mov = mult(dir_to_move(ang), n)
        pos = add(pos, mov)
    if a in "NESW":
        mov = mult(DIRS[a], n)
        pos = add(pos, mov)

print(int(abs(pos[0]) + abs(pos[1])))

print("B: ")

pos = (0, 0)
way = (10, -1)

def rot(w, angle):
    angle = radians(angle)
    c = round(cos(angle), 3)
    s = round(sin(angle), 3)
    x, y = w
    a = x * c - y * s
    b = x * s + y * c
    return a, b

for a, n in actions:
    if a == "R":
        way = rot(way, n)
    if a == "L":
        way = rot(way, -n)

    if a == "F":
        mov = mult(way, n)
        pos = add(pos, mov)
    if a in "NESW":
        mov = mult(DIRS[a], n)
        way = add(way, mov)

print(int(abs(pos[0]) + abs(pos[1])))
