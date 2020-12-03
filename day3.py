mapp = []
while True:
    try:
        mapp.append(input())
    except:
        break

bottom = len(mapp)
width = len(mapp[0])

print("A: ")

pos = [0, 0]
trees = 0
while pos[1] < bottom:
    if mapp[pos[1]][pos[0]] == "#":
        trees += 1
    pos[0] += 3
    pos[0] %= width
    pos[1] += 1

print(trees)

print("B: ")

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total_trees = 1
for s in slopes:
    pos = [0, 0]
    trees = 0
    while pos[1] < bottom:
        if mapp[pos[1]][pos[0]] == "#":
            trees += 1
        pos[0] += s[0]
        pos[0] %= width
        pos[1] += s[1]
    total_trees *= trees

print(total_trees)
