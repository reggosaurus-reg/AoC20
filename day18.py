NUMS = "1234567890"

rows = []
while True:
    try:
        i = input()
        i = i.replace("(", "( ")
        i = i.replace(")", " )")
        rows.append(i.split())
    except:
        break

def parse(row):
    #print(f"Parse {row}")
    char = row.pop(0)

    if char == "(":
        result, row = parse(row)
    else:
        result = int(char)

    while len(row):
        op = row.pop(0)
        if op == ")":
            #print(f"{result=}")
            return result, row

        char = row.pop(0)
        if char == "(":
            right, row = parse(row)
        else:
            right = int(char)


        if op == "*":
            result *= right
        if op == "+":
            result += right
    #print(f"{result=}")
    return result


def main(rows):
    #for row in rows:
    #    print(parse(row))
    #    print()

    return sum([parse(row) for row in rows])


print("A:")

print(main(rows))
