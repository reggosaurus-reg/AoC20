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
    #print(f"Parse {row}")
    char = row.pop(0)

    if char == "(":
        result, row = parse_B(row)
    else:
        result = int(char)

    while len(row):
        op = row.pop(0)
        if op == ")":
            #print(f"{result=}")
            return result, row

        char = row.pop(0)
        if char == "(":
            right, row = parse_B(row)
        else:
            right = int(char)


        if op == "*":
            result *= right
        if op == "+":
            result += right
    #print(f"{result=}")
    return result


print("A:")

print(sum([parse_A(row) for row in deepcopy(rows)]))


print("B:")

print(sum([parse_B(row) for row in deepcopy(rows)]))
