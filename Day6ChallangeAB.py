with open("./Day6ChallangeData", "r") as f:
  inputData = f.read().strip()

def has_duplicate(a):
  return any(a.count(value) > 1 for value in a)

# För att lösa uppgift A, kör varsToCompare = 3 istället.
varsToCompare = 13
index = next((i + 1 for i in range(varsToCompare, len(inputData), 1)
              if not has_duplicate([inputData[i - a] for a in range(0, varsToCompare + 1)])), 0)

print(index)
