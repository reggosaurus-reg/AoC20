starting_numbers = list(map(int, input().split(",")))
STARTERS = len(starting_numbers)

def solve(TURNS):
    spoken = {}
    last_was_new = True
    last = None

    for turn in range(1, TURNS + 1):
        if turn <= STARTERS:
            num = starting_numbers[turn - 1]
        elif last_was_new:
            num = 0
        else:
            all_spoken = spoken[last]
            num = all_spoken[-1] - all_spoken[-2]

        last_was_new = False
        if num not in spoken:
            last_was_new = True
            spoken[num] = []


        spoken[num].append(turn)
        last = num

    return last

print("A: ")

print(solve(2020))

print("B: (a bit slow, ~20s)")

print(solve(30000000))
