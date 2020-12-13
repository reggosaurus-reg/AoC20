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

buses = {}
for i, b in enumerate(all_buses):
    if b == "x":
        continue

    b = int(b)
    buses[b] = (i, (b - i) % b)

#print(buses)

max_step = max(buses.keys())
t = buses[max_step][1]
#print("start:", max_step, t)
while True:
#for _ in range(5):
    t += max_step
    print("t:", t)
    ok = True
    for b, info in buses.items():
#        print(t%b, info[1])
        if t % b != info[1]:
            ok = False
            break
    if ok:
        print("correct", t)
        break

