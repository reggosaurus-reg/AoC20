adapters = [] #list(map(int, input().readlines()))
while True:
    try:
        adapters.append(int(input()))
    except:
        break

print("A: ")

adapters = sorted(adapters)
adapters.append(adapters[-1] + 3)
diffs = []
jolts = 0
for a in adapters:
    diff = a - jolts
    diffs.append(diff)
    jolts = a

print(diffs.count(1) * diffs.count(3))

print("B: ")


adapters = [0] + adapters#[:-1]
adapters += [adapters[-1] + 3]#[:-1] # Just added this, don't know...
ways = [0 for _ in range(adapters[-1] + 1)]
sums = [[] for _ in range(adapters[-1] + 1)]
ways[0] = 1
sums[0] = [0]

for i, a in enumerate(adapters):
    ... #print(i, a)

for i in range(1, len(adapters)):
    for a in adapters:
        roof = False
        for num in sums[i - 1]:
            roof = a > num + 3
            if roof or a <= num:
                continue
            sums[i].append(a)
            ways[i] += 1
       #     if i < 3:
       #         print(a, sums[i])
       # if i < 3:
       #     print()
        if roof: break
    if ways[i] < ways[i - 1]:
        break

print(sums[:3])
#print(sums, ways)
print(max(ways))
