from copy import deepcopy

global_rules = {}
while True:
    row = input()
    if row == "":
        break

    num, rest = row.split(":")
    num = int(num)
    rest = rest.strip()

    if rest.startswith("\""):
        match = rest.strip("\"")
    else:
        match = []
        for seq in rest.split("|"):
            match.append(list(map(int, seq.split())))

    global_rules[num] = match

messages = []
while True:
    try:
        row = input()
    except:
        break
    messages.append(row)


def can_be_constructed(m, to_expand):
    if not m or not to_expand:
        return not m and not to_expand

    rules = global_rules[to_expand.pop(0)]
    if isinstance(rules, str):
        if m[0] == rules:
            return can_be_constructed(m[1:], to_expand)
        else:
            return False

    for rule in rules:
        if can_be_constructed(m, rule + to_expand):
            return True
    return False


print("A:")

print(len([m for m in messages if can_be_constructed(m, [0])]))


print("B:")

global_rules[8].append([42, 8])
global_rules[11].append([42, 11, 31])

print(len([m for m in messages if can_be_constructed(m, [0])]))
