with open("./Day5ChallangeData", "r") as f:
    stackData = f.readlines()

with open("./Day5ChallangeData2", "r") as g:
    schemeData = g.readlines()

stacksArray = []

for i in range(10, len(stackData), 1):
    stackNumber, stackString = stackData[i].split(" ", 1)
    currentStack = []
    for a in range(len(stackString.strip())):
        currentStack.append(stackString[a])

    stacksArray.append(currentStack)

#print(stacksArray)

fromStack = 0
targetStack = 0
nrOfCrates = 0

for i in range(len(schemeData)):
    worthless1, nrOfCrates, worthless2, fromStack, worthless3, targetStack = schemeData[i].strip().split(" ")
    nrOfCrates = int(nrOfCrates)
    fromStack = int(fromStack)
    targetStack = int(targetStack)

    temp = stacksArray[fromStack - 1][-nrOfCrates:]
    print(temp)
    stacksArray[fromStack - 1] = stacksArray[fromStack - 1][:-nrOfCrates]
    stacksArray[targetStack - 1].extend(temp)

print(stacksArray)



