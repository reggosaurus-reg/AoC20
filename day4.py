REQUIRED = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

def take_input():
    all_passports = []
    while True:
        passport = {}
        while True:
            try:
                row = input().split()
            except:
                return all_passports
            if row:
                for entry in row:
                    k, v = entry.split(":")
                    passport[k] = v
            else:
                break
        all_passports.append(passport)


print("A: ")
all_passports = take_input()
valid_passports = []
for passport in all_passports:
    fields = passport.keys()
    passed = True
    for r in REQUIRED:
        if r not in fields:
            passed = False
            break
    if passed:
        valid_passports.append(passport)
print(len(valid_passports))

print("B: ")

valid = 0
for passport in valid_passports:
    byr = passport["byr"]
    if len(byr) != 4:
        continue
    try:
        byr = int(byr)
    except:
        continue
    if byr < 1920 or byr > 2002:
        continue

    iyr = passport["iyr"]
    if len(iyr) != 4:
        continue
    try:
        iyr = int(iyr)
    except:
        continue
    if iyr < 2010 or iyr > 2020:
        continue

    eyr = passport["eyr"]
    if len(eyr) != 4:
        continue
    try:
        eyr = int(eyr)
    except:
        continue
    if eyr < 2020 or eyr > 2030:
        continue

    hgt = passport["hgt"]
    if hgt[-2:] == "cm":
        h = int(hgt[:-2])
        if h < 150 or h > 193:
            continue
    elif hgt[-2:] == "in":
        h = int(hgt[:-2])
        if h < 59 or h > 76:
            continue
    else:
        continue

    hcl = passport["hcl"]
    if hcl[0] != "#":
        continue
    color = hcl[1:]
    if len(color) != 6:
        if not (color.isalnum() and color.islower()):
            continue

    ecl = passport["ecl"]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue

    pid = passport["pid"]
    if len(pid) != 9:
        continue
    try:
        int(pid)
    except:
        continue

    valid += 1

print(valid)
