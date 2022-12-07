with open('Day7ChallangeData', 'r') as file:
    lines = file.readlines()

totalSize = 100000
outerMostDir = {
    "size": 0
}
currentDir = outerMostDir
navigatorStack = []


def get_sum_size(input_dict):
    if len(input_dict.items()) == 1:
        print("Halloj", input_dict)
        return input_dict["size"]
    s = input_dict["size"]
    for child in input_dict.items():
        if not child[0] == "size":
            s += get_sum_size(child[1])
    return s


sizes = []


def collect_tiny_sums(input_dict):
    temp = get_sum_size(input_dict)
    #if temp <= 100000:
    sizes.append(temp)
    for child in input_dict.items():
        if not child[0] == "size":
            collect_tiny_sums(child[1])


for i in range(len(lines)):
    lines[i] = lines[i].strip()
    if lines[i].startswith("$ ls"):
        a = 1
        dirSize = 0
        while True:
            if lines[i + a].startswith("$"):
                break
            if "dir" in lines[i + a]:
                a += 1
                continue
            fileSize, fileName = lines[i + a].split(" ")
            fileName = fileName.strip()
            fileSize = int(fileSize)
            print(fileSize, fileName)
            currentDir["size"] += fileSize
            a += 1

        print("Done with loop. dirSize =", dirSize)
    elif lines[i].startswith("$ cd"):
        targetDir = lines[i].split(" ")[2]
        if targetDir == "..":
            navigatorStack.pop()
        else:
            navigatorStack.append(targetDir)
            currentDir = outerMostDir
            for x in navigatorStack:
                if x in currentDir:
                    currentDir = currentDir[x]
                else:
                    currentDir[x] = {"size": 0}
                    currentDir = currentDir[x]
        print(navigatorStack)

print("Hej", outerMostDir)
collect_tiny_sums(outerMostDir)
totalSizeInUse = sizes[0]
print(sizes)
print("A:", sum(sizes))
print("Available:", 70000000 - totalSizeInUse)

sizes.pop(0)
sizes.pop(0)

#We need to free 8518336
needToFree = 8518336
newList = []

for s in sizes:
    if s >= needToFree:
        newList.append(s)

print(min(newList))