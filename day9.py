PREAMBLE = 25

all_numbers = []


while True:
    try:
        num = int(input())
    except:
        break

    all_numbers.append(num)

print("A: ")

def is_valid(num, start, end):
    sums = set()
    for i in range(start, end):
        for j in range(i + 1, end):
            a = all_numbers[i]
            b = all_numbers[j]
            if a == b:
                continue
            sums.add(a + b)

    return num in sums


B_number = None

for i, n in enumerate(all_numbers):
    if i < PREAMBLE: continue

    if not is_valid(n, i - PREAMBLE, i):
        B_number = n
        break

print(B_number)

print("B: ")

start = 0
end = 0
curr_sum = B_number + 1

for i, num in enumerate(all_numbers):
    if curr_sum == B_number:
        break
    else:
        curr_sum = num

    for j in range(i + 1, len(all_numbers)):
        curr_sum += all_numbers[j]
        if curr_sum >= B_number:
            start = i
            end = j
            break



contiguous_range = all_numbers[start:end]
print(min(contiguous_range) + max(contiguous_range))










    #if len(all_numbers) == PREAMBLE:
    #    for i, a in enumerate(all_numbers):
    #        for b in all_numbers[i + 1:]:
    #            if a == b:
    #                continue
    #            print(a, b)
    #            sums.add(a + b)

    #if len(all_numbers) > PREAMBLE:
    #    if num not in sums:
    #        print(num)
    #        break

