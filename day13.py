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

from math import gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def lcm_rec(seq):
    i, b, d = seq[-1]
    if len(seq) == 1: # Check last two together?
        return b
    else:
        return lcm(b, lcm_rec(seq[:-1])) - i

t = float("inf")
buses = [(i, int(b), (int(b) - i) % int(b))
            for i, b in enumerate(all_buses) if b != "x"]

t = lcm_rec(buses)
print(t)
#t = 1068781

for i, b, d in buses:
    if t % b == d:
        print(True)
    print(i, b, d, ":", t % b)
