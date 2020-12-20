from copy import deepcopy

rules = {}

while True:
    row = input()
    if row == "":
        break

    num, rest = row.split(":")
    num = int(num)
    rest = rest.strip()

    if rest.startswith("\""):
        match = [rest.strip("\"")]
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
valid_messages = [m for m in messages if m in valid]
print(len(valid_messages))
print(rules[42])
print(rules[11] == rules[42] + rules[31])

print("B:")

#rules_B[8] = [[42], [42, 8]]
#rules_B[11] = [[42, 31], [42, 11, 31]]

for m in [m for m in messages if m not in valid]:
    FORTYTWO = rules[42]
    LENGTH = len(FORTYTWO[0])
    m8 = m
    match8 = True
    while m8:
        if m8[:LENGTH] in FORTYTWO:
            m8 = m8[LENGTH:]
            continue
        match8 = False
        break
    if match8:
        print("Matched 8!")
        valid_messages.append(m)
        continue


print(len(valid_messages))

#print([expand(0, m) for m in messages])
