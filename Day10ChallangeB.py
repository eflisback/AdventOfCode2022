with open('Day10ChallangeData', 'r') as file:
    lines = file.readlines()
lines = [item.strip() for item in lines]
x = 1
previousCmd = ""
cycle = 1
cycleEachValue = []
rowInit = ". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."

table = [
    rowInit.split(" "),
    rowInit.split(" "),
    rowInit.split(" "),
    rowInit.split(" "),
    rowInit.split(" "),
    rowInit.split(" ")
]


def updateList(c, x):
    row = int(c/40)
    rest = (c - 1) % 40
    print(c, x, row, rest)
    if rest == x or rest == x + 1 or rest == x - 1:
        table[row][rest] = '#'

    if {'cycle': c, 'x': x} not in cycleEachValue:
        cycleEachValue.append({'cycle': c, 'x': x})


for line in lines:
    if "noop" in line:
        updateList(cycle, x)
        cycle += 1

    else:
        addedNumber = int(line.split(" ")[1])
        updateList(cycle, x)
        cycle += 1
        updateList(cycle, x)
        cycle += 1
        x += addedNumber
    updateList(cycle, x)

for a in range(len(table)):
    print("".join(table[a]), a)

#FCJAPJRE