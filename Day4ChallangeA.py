f = open("./Day4ChallangeData", "r")
lines = f.readlines()

sum = 0

for i in range(len(lines)):
    row = lines[i]
    elfA = row[0:int(row.find(','))]
    elfB = row[int(1 + (row.find((',')))):int(len(row))]
    #print(elfA, " - ", elfB)

    elfAStart = int(elfA[0:int(elfA.find('-'))])
    elfAEnd = int(elfA[(1 + elfA.find('-')):int(len(elfA))])

    elfBStart = int(elfB[0:int(elfB.find('-'))])
    elfBEnd = int(elfB[(1 + elfB.find('-')):int(len(elfB))])

    #print(elfAStart, elfAEnd)
    #print(elfBStart, elfBEnd)

    if elfAStart <= elfBStart and elfAEnd >= elfBEnd or elfBStart <= elfAStart and elfBEnd >= elfAEnd:
        sum += 1

print(sum)