adapters = []
while True:
    try:
        adapters.append(int(input()))
    except:
        break

print("A: ")

adapters = sorted(adapters)
adapters = [0] + adapters + [adapters[-1] + 3]
diffs = []
jolts = 0
for a in adapters:
    diff = a - jolts
    diffs.append(diff)
    jolts = a

print(diffs.count(1) * diffs.count(3))


print("B: ")

sums = [0 for _ in range(adapters[-1] + 1)]

for i in adapters:
    if i == 0:
        sums[i] = 1
    elif i == 1:
        sums[i] = sums[i-1]
    elif i == 2:
        sums[i] = sums[i-1] + sums[i-2]
    else:
        sums[i] = sums[i-1] + sums[i-2] + sums[i-3]

print(sums[-1])
