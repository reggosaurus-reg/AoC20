allergens = {}  # allergen: ingredient, One to one
ing_app = {}  # appearances
alg_app = {}  # appearances
required = {}

# If listed, the allergen is in one of the ingredients. If not listed, might still be!

while True:
    try:
        food = input()
    except:
        break

    i, a = food.split("(")
    i = i.split()
    a = a[:-1].split()[1:]

    for ing in i:
        if ing not in ing_app:
            ing_app[ing] = 0
        ing_app[ing] += 1

    for alg in a:
        alg = alg.strip(",")
        if alg not in allergens:
            required[alg] = []
            allergens[alg] = []
            alg_app[alg] = 0
        allergens[alg] += i
        required[alg].append(i)
        alg_app[alg] += 1


print("A:")

impossible = {i: [] for i in ing_app.keys()}

for alg in allergens.keys():
    num = alg_app[alg]
    ingredients = allergens[alg]

    for i in impossible.keys():
        if ingredients.count(i) != num:
            impossible[i].append(alg)

LEN = len(allergens.keys())
UNHARMFUL = [i for i, n in impossible.items() if len(n) == LEN]
print(sum([ing_app[i] for i in UNHARMFUL]))


print("B:")

for a in allergens:
    allergens[a] = set([i for i in allergens[a] if i not in UNHARMFUL])
    new = []
    for food in required[a]:
        new.append(set([i for i in food if i not in UNHARMFUL]))
    required[a] = []
    LEN = len(new)
    all = []
    for seq in new:
        for item in seq:
            all.append(item)
    for ing in new[0]:
        if all.count(ing) == LEN:
            required[a].append(ing)

to_assign = sorted(required.keys(), key=lambda a: len(required[a]))
assigned = {a: None for a in required.keys()}
for alg in to_assign:
    for ing in required[alg]:
        if ing in assigned.values() or ing in UNHARMFUL:
            continue
        assigned[alg] = ing

print(",".join([i for a, i in sorted(assigned.items())]))
