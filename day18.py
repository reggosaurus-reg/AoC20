from copy import deepcopy

rows = []
while True:
    try:
        i = input()
        i = i.replace("(", "( ")
        i = i.replace(")", " )")
        rows.append(i.split())
    except:
        break

def parse_A(row):
    char = row.pop(0)
    if char == "(":
        result, row = parse_A(row)
    else:
        result = int(char)

    while len(row):
        op = row.pop(0)
        if op == ")":
            return result, row

        char = row.pop(0)
        if char == "(":
            right, row = parse_A(row)
        else:
            right = int(char)

        if op == "*":
            result *= right
        if op == "+":
            result += right
    return result

def parse_B(row):
    new_row = []

    char = row.pop(0)
    if char == "(":
        inner_new, row = parse_B(row)
        result = parse_A(["("] + inner_new + [")"])
    else:
        result = int(char)

    while len(row):
        op = row.pop(0)
        if op == ")":
            new_row.append(result)
            return new_row, row

        char = row.pop(0)
        if char == "(":
            inner_new, row = parse_B(row)
            right = parse_A(["("] + inner_new + [")"])
        else:
            right = int(char)

        if op == "*":
            new_row.append(result)
            new_row.append("*")
            result = right
        if op == "+":
            result += right
    new_row.append(result)

    a = parse_A(new_row)
    return a


print("A:")

print(sum([parse_A(row) for row in deepcopy(rows)]))


print("B:")

print(sum([parse_B(row) for row in deepcopy(rows)]))
