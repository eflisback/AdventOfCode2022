with open('Day10ChallangeData', 'r') as file:
    lines = file.readlines()
lines = [item.strip() for item in lines]
x = 1
previousCmd = ""
cycle = 1
cycleEachValue = []


def updateList(c, v):
    if {'cycle': c, 'x': v} not in cycleEachValue:
        cycleEachValue.append({'cycle': c, 'x': v})


for line in lines:
    print(line)
    if "noop" in line:
        updateList(cycle, x)
        cycle += 1
        print("nooped")

    else:
        addedNumber = int(line.split(" ")[1])
        updateList(cycle, x)
        cycle += 1
        updateList(cycle, x)
        cycle += 1
        x += addedNumber
    updateList(cycle, x)

print(cycleEachValue)
print(cycleEachValue[19]['cycle'] * cycleEachValue[19]['x'] + cycleEachValue[59]['cycle'] * cycleEachValue[59]['x']
      + cycleEachValue[99]['cycle'] * cycleEachValue[99]['x'] + cycleEachValue[139]['cycle'] * cycleEachValue[139]['x']
      + cycleEachValue[179]['cycle'] * cycleEachValue[179]['x'] + cycleEachValue[219]['cycle']
      * cycleEachValue[219]['x'])
