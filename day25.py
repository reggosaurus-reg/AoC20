DOOR_KEY = int(input())
CARD_KEY = int(input())

def find_loop_size(res):
    value = 1
    loop = 0
    while value != res:
        value *= 7
        value = value % 20201227
        loop += 1
    return loop

def transform(sub, loop):
    value = 1
    for _ in range(loop):
        value *= sub
        value = value % 20201227
    return value



print("A:")

card_loop = find_loop_size(CARD_KEY)
door_loop = find_loop_size(DOOR_KEY)

encryption_key = transform(DOOR_KEY, card_loop)
if transform(CARD_KEY, door_loop) != encryption_key:
    print("Something wrong")

print(encryption_key)
