start = int(input())
all_buses = input().split(",")
buses = list(map(int, filter(lambda x: x != "x", all_buses)))

print("A: ")

earliest = float("inf")
bus = 0
wait = 0

for b in buses:
    last = start - start % b
    now = last + b
    if now < earliest:
        earliest = now
        bus = b
        wait = now - start

print(bus * wait)

print("B: ")

from sympy.ntheory.modular import crt

moduli = []
residues = []
for i, b in enumerate(all_buses):
    if b == "x":
        continue

    b = int(b)
    moduli.append(b)
    residues.append((b - i) % b)

print(crt(moduli, residues)[0])
