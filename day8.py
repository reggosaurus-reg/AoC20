from copy import deepcopy

def opr(row): return row[0]

def arg1(row): return row[1]


class GameConsole():
    def __init__(me):
        me.oplist = []
        me.accumulator = 0
        me.pointer = 0

        me.has_visited = set()
        me.could_terminate = True

    def take_input(me):
        while True:
            try:
                row = input().split()
            except:
                break

            for i, arg in enumerate(row[1:]):
                row[i+1] = int(arg)
            me.oplist.append(row)

    def perform_one_operation(me):
        row = me.oplist[me.pointer]
        op = opr(row)

        if op == "acc":
            me.accumulator += arg1(row)
            me.pointer += 1
        if op == "jmp":
            me.pointer += arg1(row)
        if op == "nop":
            me.pointer += 1

    def run(me):
        max_pointer = len(me.oplist) - 1
        while me.pointer < max_pointer:
            if me.pointer in me.has_visited:
                me.could_terminate = False
                return

            me.has_visited.add(me.pointer)
            me.perform_one_operation()

        me.could_terminate = True

    def reset(me):
        me.accumulator = 0
        me.pointer = 0
        me.has_visited = set()
        me.could_terminate = True

    def main(me):
        me.take_input()
        me.run()

print("A: ")
gc = GameConsole()
# gc.main()  # Somehow this row makes B crash...
print(gc.accumulator)

print("B: ")
gc = GameConsole()
gc.main()
i = 0
original_oplist = deepcopy(gc.oplist)
while not gc.could_terminate:
    gc.reset()
    gc.oplist = deepcopy(original_oplist)
    while True:
        op = opr(gc.oplist[i])
        if op == "acc":
            i += 1
            continue
        if op == "jmp":
            gc.oplist[i][0] = "nop"
            i += 1
            break
        if op == "nop":
            gc.oplist[i][0] = "jmp"
            i += 1
            break
    gc.run()

gc.perform_one_operation()  # Very ugly hack... and A & B still won't work together.
print(gc.accumulator)
