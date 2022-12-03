f = open("./Day3ChallangeData", "r")
lines = f.readlines()
sum = 0

alfabet = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
timesPrint = 0

for i in range(0, len(lines), 3):
    found = False
    row1 = lines[i].strip('\n')
    row2 = lines[i+1].strip('\n')
    row3 = lines[i+2].strip('\n')

    for a in range(len(row1)):
        checkLetter = row1[a]

        for b in range(len(row2)):
            if checkLetter == row2[b]:
                for c in range(len(row3)):
                    if checkLetter == row3[c] and not found:
                        sum += alfabet.find(checkLetter)
                        print(checkLetter, alfabet.find(checkLetter))
                        timesPrint += 1
                        found = True

print(sum, timesPrint)