rules = {}
expanded = set()
while True:
    row = input()
    if row == "":
        break

    num, rest = row.split(":")
    num = int(num)
    rest = rest.strip()

    if rest.startswith("\""):
        match = [rest.strip("\"")]
        expanded.add(num)
    else:
        match = []
        for seq in rest.split("|"):
            match.append(list(map(int, seq.split())))

    rules[num] = match


def expand(num):
    result = []
    for x in rules[num]:
        if isinstance(x, str):
            result.append(x)
        elif isinstance(x, list):
            left = expand(x[0])
            try:
                right = expand(x[1])
            except:
                right = []
            combos = []
            if not right:
                combos += left
            else:
                for l in left:
                    for r in right:
                        combos.append("".join(l + r))

            result += combos

    expanded.add(num)
    rules[num] = result
    return result

messages = []
while True:
    try:
        row = input()
    except:
        break
    messages.append(row)

print("A:")

valid = expand(0)
print(len([m for m in messages if m in valid]))
