with open('Day1ChallangeData') as f:
    lines = f.readlines()

# Number of top calorie-holders to sum
topElves = 3

elvesTotCal = []
currentElfCal = 0

for i in range(len(lines)):
    if lines[i] != '\n':
        currentElfCal += int(lines[i])
    else:
        elvesTotCal.append(currentElfCal)
        currentElfCal = 0

elvesTotCal.sort(reverse=True)
calSum = 0
for i in range(topElves):
    calSum += elvesTotCal[i]

print(calSum)
