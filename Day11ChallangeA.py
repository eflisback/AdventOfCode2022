with open('Day11ChallangeData', 'r') as file:
    lines = file.readlines()
lines = [item.strip() for item in lines]


class Monkey:
    def __init__(self):
        self.inspectedItems = 0
        self.operation = ""
        self.operationVal = ""
        self.divideInt = 0
        self.inventory = []
        self.trueTarget = 0
        self.falseTarget = 0


monkeys = []


def populate_list():
    currentMonkey = 0
    for line in lines:
        if "Monkey" in line:
            currentMonkey = int(line.split(" ")[1].replace(":", ""))
            #print(currentMonkey)
            newMonkey = Monkey()
            #newMonkey.inventory = []
            #newMonkey.divideInt = 0
            #newMonkey.operationVal = 0
            #newMonkey.operation = ""
            monkeys.append(newMonkey)
        elif "Starting items" in line:
            valuesStr = line.split(": ")[1].strip().split(", ")
            valuesStr = map(int, valuesStr)
            valuesInt = list(valuesStr)
            monkeys[currentMonkey].inventory = valuesInt
            #print(valuesInt)
        elif "Operation" in line:
            opString = line.split("= old ")[1].split(" ")[0]
            opValue = line.split("= old ")[1].split(" ")[1]
            monkeys[currentMonkey].operation = opString
            monkeys[currentMonkey].operationVal = opValue
            #print(opString, opValue)
        elif "Test" in line:
            divideInt = int(line.split("divisible by ")[1])
            monkeys[currentMonkey].divideInt = divideInt
            #print(divideInt)
        elif "If true" in line:
            trueTarget = int(line.split("to monkey ")[1])
            monkeys[currentMonkey].trueTarget = trueTarget
            #print(trueTarget)
        elif "If false" in line:
            falseTarget = int(line.split("to monkey ")[1])
            monkeys[currentMonkey].falseTarget = falseTarget
            #print(falseTarget)


populate_list()




for i in range(20):
    #print(len(monkeys))
    if i % 100 == 0:
        print("100 iterations done")
    for a in range(len(monkeys)):
        if monkeys[a].inventory:
            for b in range(len(monkeys[a].inventory)):
                monkeys[a].inspectedItems += 1
                worry = monkeys[a].inventory[0]
                monkeys[a].inventory.pop(0)
                change = 0
                if monkeys[a].operationVal != "old":
                    change = int(monkeys[a].operationVal)
                else:
                    change = worry
                if monkeys[a].operation == "+":
                    worry += change
                elif monkeys[a].operation == "*":
                    worry *= change
                worry = int(worry / 3)
                if worry % monkeys[a].divideInt == 0:
                    monkeys[monkeys[a].trueTarget].inventory.append(worry)
                else:
                    monkeys[monkeys[a].falseTarget].inventory.append(worry)

topInspectorsList = []
for monkey in monkeys:
    topInspectorsList.append(monkey.inspectedItems)

topInspectorsList = sorted(topInspectorsList, reverse=True)
print(topInspectorsList[0] * topInspectorsList[1])
