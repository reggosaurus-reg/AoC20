all_bags = {}
inversed_bags = {}
while True:
    try:
        row = input().split()
    except:
        break

    bag = ""
    i = 0
    contains = []
    for i, word in enumerate(row):
        if word == "contain":
            break
        if word.startswith("bag"):
            continue
        else:
            bag += word
    row = row[i + 1:]
    all_bags[bag] = []

    in_bag = ""
    num = 0
    for word in row:
        if word == "no":
            break

        if word.startswith("bag"):
            all_bags[bag].append((in_bag, num))

            if in_bag not in inversed_bags:
                inversed_bags[in_bag] = []
            inversed_bags[in_bag].append(bag)

            in_bag = ""
            continue

        try:
            num = int(word)
        except:
            in_bag += word

# A

print("A: ")
can_hold = set()
current = ""
to_expand = ["shinygold"]
while to_expand:
    current = to_expand.pop(0)
    can_hold.add(current)
    try:
        expand = inversed_bags[current]
    except:
        continue

    for bag in expand:
        to_expand.append(bag)

print(len(can_hold) - 1) # Don't count shinygold

# B

print("B: ")
can_hold = []
current = ""
to_expand = [("shinygold", 1)]
count = 0
while to_expand:
    current, num = to_expand.pop(0)
    can_hold.append(current)
    count += num
    try:
        expand = all_bags[current]
    except:
        continue

    for b, n in expand:
        to_expand.append((b, n*num))

print(count - 1) # Don't count shinygold
