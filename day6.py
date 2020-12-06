import string
totalA = 0
totalB = 0
START_B = list(string.ascii_lowercase)

def main():
    global totalA
    global totalB

    while True:
        groupA = set()
        groupB = START_B[:]
        while True:
            # Input
            try:
                person = input()
            except:
                return

            if not person:
                break

            # A
            for letter in person:
                groupA.add(letter)

            # B
            for x in groupB[:]:
                if x not in person:
                    groupB.remove(x)

        totalA += len(groupA)
        totalB += len(groupB)

main()

print("A: ")
print(totalA)

print("B: ")
print(totalB)
