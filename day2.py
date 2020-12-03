Accepted = 0
Bccepted = 0
while True:
    try:
        row = input()
    except:
        break

    p, pwd = row.split(":")
    pwd = pwd.strip()
    i, letter = p.split()
    low, high = list(map(int, i.split("-")))

    if low <= pwd.count(letter) <= high:
        Accepted += 1

    if (pwd[low-1] == letter) != (pwd[high-1] == letter):
        Bccepted += 1

print("A: ")
print(Accepted)

print("B: ")
print(Bccepted)
