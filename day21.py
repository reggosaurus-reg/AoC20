allergens = {}  # allergen: ingredient, One to one
ing_app = {}  # appearances
alg_app = {}  # appearances

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
            allergens[alg] = []
            alg_app[alg] = 0
        allergens[alg] += i
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
print(sum([ing_app[i] for i, n in impossible.items() if len(n) == LEN]))


print("B:")
#to_assign = sorted(allergens.keys(), key=lambda a: len(allergens[a]))
#assigned = {a: None for a in allergens.keys()}
#while to_assign: #any(map(lambda i: i is None, assigned.values())):
#    alg = to_assign.pop(0)
#    print(alg)
#    for ing in allergens[alg]:
#        if ing in assigned.values():
#            continue
#        assigned[alg] = ing
#print(assigned)
#
#for i in ingredients:
#    if i not in assigned:
#        print(i)

