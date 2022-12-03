f = open("./Day3ChallangeData", "r")
lines = f.readlines()
sum = 0

alfabet = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
timesPrint = 0
found = False

for i in range(len(lines)):
    found = False
    row = lines[i].strip('\n')
    middle = len(row)/2
    item1 = row[0:int(middle)]
    item2 = row[int(middle):int(len(row))]

    for a in range(len(item1)):
        checkLetter = item1[a]

        for b in range(len(item2)):
            if checkLetter == item2[b] and not found:
                sum += alfabet.find(checkLetter)
                found = True
                print(checkLetter, ", ", alfabet.find(checkLetter))
                timesPrint += 1

print(sum)
