# Parse categories
categories = {}
while True:
    row = input().split(":")
    if not row[0]:
        break

    cat = row[0]
    row = row[1].split()
    valid_nums = set()
    range1 = row[0]
    range2 = row[2]

    a, b = map(int, range1.split("-"))
    for n in range(a, b+1):
        valid_nums.add(n)
    a, b = map(int, range2.split("-"))
    for n in range(a, b+1):
        valid_nums.add(n)

    categories[cat] = valid_nums

# Parse my ticket
input()
my_ticket = list(map(int, input().split(",")))

# Parse other tickets
input()
input()
tickets = []
while True:
    try:
        ticket = list(map(int, input().split(",")))
    except:
        break
    tickets.append(ticket)


print("A: ")

invalid_values = []
tickets_to_keep = []
for ticket in tickets:
    ok_ticket = True
    for n in ticket:
        invalid = True
        for ok in categories.values():
            if n in ok:
                invalid = False
        if invalid:
            invalid_values.append(n)
            ok_ticket = False
    if ok_ticket:
        tickets_to_keep.append(ticket)

print(sum(invalid_values))


print("B: ")

possible_cats = [{cat: len(tickets) for cat in categories.keys()}
                 for _ in tickets[0]]

for ticket in tickets_to_keep:
    for i, n in enumerate(ticket):
        for cat, ok in categories.items():
            if n not in ok:
                possible_cats[i][cat] -= 1

# Filter possible ones
for d in possible_cats:
    for c, v in list(d.items()):
        if v != len(tickets):
            del d[c]

# Assign in turns and save index for unique ones
indices = {}
assigned = "assigned categories this round"
while assigned:
    assigned = []
    for i, d in enumerate(possible_cats):
        if len(d.keys()) == 1:
            cat = list(d.keys())[0]
            indices[cat] = i
            assigned.append(cat)
    for d in possible_cats:
        for cat in assigned:
            if cat in d:
                del d[cat]

result = 1
for cat in categories:
    if cat.startswith("departure"):
        result *= my_ticket[indices[cat]]

print(result)
