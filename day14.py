program = []

while True:
    try:
        left, _, right = input().split()
    except:
        break
    if left == "mask":
        mask = list(right)
        for i, b in enumerate(mask):
            if b == "X":
                continue
            mask[i] = int(b)
        program.append(("mask", mask))
    elif left[:3] == "mem":
        adr = int(left[4:-1])
        num = int(right)
        program.append(("mem", (adr, num)))


print("A:")

memory = {}
mask = None

for left, right in program:
    if left == "mask":
        mask = right
    elif left == "mem":
        adr, num = right

        num_bin = [int(n) for n in bin(num)[2:]]
        num_len = len(num_bin)
        mask_len = len(mask)

        num_list = [0 for _ in range(mask_len - num_len)] + list(num_bin)

        for i, b in enumerate(mask):
            if b == "X":
                continue
            num_list[i] = b

        num = int("".join(map(str,num_list)), 2)
        memory[adr] = num

print(sum(memory.values()))


print("B:")

memory = {}
mask = None

for left, right in program:
    if left == "mask":
        mask = right
    elif left == "mem":
        adr, num = right

        adr_bin = [int(n) for n in bin(adr)[2:]]
        adr_len = len(adr_bin)
        mask_len = len(mask)

        adr_list = [0 for _ in range(mask_len - adr_len)] + list(adr_bin)

        for i, b in enumerate(mask):
            if b == 0:
                continue
            adr_list[i] = b

        first_index = min(adr_list.index(1), adr_list.index("X"))
        adr_list = adr_list[first_index:]

        parents = [adr_list]
        addresses = []
        while parents:
            p = parents.pop(0)
            try:
                i = p.index("X")
            except ValueError:
                p = int("".join(map(str,p)), 2)
                addresses.append(p)
                continue

            a = p[:i] + [0] + p[i+1:]
            b = p[:i] + [1] + p[i+1:]
            parents.append(a)
            parents.append(b)

        for a in addresses:
            memory[a] = num

print(sum(memory.values()))
