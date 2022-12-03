with open('Day1ChallangeData') as f:
    lines = f.readlines()

elvesTotCal = []
currentElfCal = 0

for i in range(len(lines)):
    if lines[i] != '\n':
        currentElfCal += int(lines[i])
    else:
        elvesTotCal.append(currentElfCal)
        currentElfCal = 0

print(max(elvesTotCal))
