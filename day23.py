cups_initial = [int(num) for num in input()]

print("A:")

MOVES = 100
SIZE = len(cups_initial)

cups = cups_initial[:]

for _ in range(MOVES):
    i = 0
    curr = cups[0]
    picked = [cups.pop(1), cups.pop(1), cups.pop(1)]
    dest = None
    temp = curr - 1
    while dest not in cups:
        temp -= 1
        dest = temp % SIZE + 1
    d = cups.index(dest)
    cups = cups[:(d + 1) % SIZE] + picked + cups[(d + 1) % SIZE:]
    cups = cups[i + 1:] + cups[:i + 1]  # Always place curr in beginning

i = cups.index(1)
cups = cups[i:] + cups[:i]
print("".join(map(str, cups[1:])))


print("B:")

MOVES = 10000000
SIZE = 1000000

cups = cups_initial[:] + [x for x in range(10, SIZE + 1)]

# Well... I will have to calculate it, not simulate it. Obviously.
for _ in range(MOVES):
    i = 0
    curr = cups[0]
    picked = [cups.pop(1), cups.pop(1), cups.pop(1)]
    dest = None
    temp = curr - 1
    while dest not in cups:
        temp -= 1
        dest = temp % SIZE + 1
    d = cups.index(dest)
    cups = cups[:(d + 1) % SIZE] + picked + cups[(d + 1) % SIZE:]
    cups = cups[i + 1:] + cups[:i + 1]  # Always place curr in beginning

i = cups.index(1)
print(cups[i+1], cups[i+2])

