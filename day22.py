from copy import copy

player1 = []
player2 = []

input()
while True:
    card = input()
    if card == "":
        break
    player1.append(int(card))

input()
while True:
    card = input()
    if card == "":
        break
    player2.append(int(card))


def score(player):
    LEN = len(player)
    return sum([x * (LEN - i) for i, x in enumerate(player)])


print("A:")

def combat(player1, player2):
    while player1 and player2:
        p1 = player1.pop(0)
        p2 = player2.pop(0)

        if p1 > p2:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)

    if player1:
        print(score(player1))
    if player2:
        print(score(player2))

combat(copy(player1), copy(player2))

print("B:")

def recursive_combat(player1, player2):
    deals = {1: [], 2: []}
    while player1 and player2:
        p1 = player1.pop(0)
        p2 = player2.pop(0)

        # Instawin?
        if player1 in deals[1] and player2 in deals[2]:
            return 1

        deals[1].append(copy(player1))
        deals[2].append(copy(player2))

        # Recursion?
        if len(player1) >= p1 and len(player2) >= p2:
            winner = recursive_combat(copy(player1[:p1]),
                                      copy(player2[:p2]))

        # Normal
        elif p1 > p2:
            winner = 1
        else:
            winner = 2

        if winner == 1:
            player1.append(p1)
            player1.append(p2)
        elif winner == 2:
            player2.append(p2)
            player2.append(p1)

    if player1:
        return 1
    else:
        return 2

winner = recursive_combat(player1, player2)

if winner == 1:
    print(score(player1))
elif winner == 2:
    print(score(player2))

