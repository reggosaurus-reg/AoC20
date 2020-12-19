NUMS = "1234567890"

rows = []
while True:
    try:
        rows.append(input())
    except:
        break

def parse(row):
    print(row)
    left = ""
    op = ""
    right = ""
    jump_index = 0
    end = len(row) - 1
    for i, x in enumerate(row):
        if jump_index and i < jump_index:
            continue
        #print(x, ":", left, op, right)
        if x in NUMS:
            if op:
                right += x
            else:
                left += x
        elif x in "+*":
            op = x
        elif x == "(":
            i_start = i + 1
            i_end = i_start + row[i_start:].index(")")
            parentheses = row[i_start:i_end]
            #print("P :", parentheses)
            right = parse(parentheses)
            jump_index = i_end

        if x == " " or i == end:
            if right:
                left = evaluate(left, op, right)
                op = ""
                right = ""
    #print("L :", left)
    return left


def evaluate(left, op, right):
    left = int(left)
    right = int(right)
    #print(left, op, right)
    if op == "+":
        return left + right
    elif op == "*":
        return left * right

def main(rows):
    for row in rows:
        print(parse(row))


print("A:")

main(rows)
