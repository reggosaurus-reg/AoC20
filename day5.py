ids = []
max_id = 0
while True:
    try:
        code = input()
    except:
        break

    low = 0
    high = 127
    for x in code[:7]:
        if x == "F":
            high -= int((high + 1 - low) / 2)
        if x == "B":
            low += int((high + 1 - low) / 2)

    row = low

    low = 0
    high = 7
    column = 0
    for x in code[7:]:
        if x == "L":
            high -= int((high + 1 - low) / 2)
        if x == "R":
            low += int((high + 1 - low) / 2)
    column = low

    new_id = 8 * row + column
    ids.append(new_id)

print("A: ")
print(max(ids))

print("B: ")
for seat in range(1, max(ids)):
    if seat not in ids and \
       seat - 1 in ids and seat + 1 in ids:
        print(seat)
        break
