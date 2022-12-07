with open('Day7ChallangeData', 'r') as file:
    lines = file.readlines()

totalSize = 100000
outermost = {}
currentPath = outermost


for i in range(len(lines)):
    lines[i] = lines[i]
    if lines[i][0] == '$':
        if "cd" in lines[i]:
            currentPath = lines[i][-1]
    elif "dir" in lines[i]:
        currentPath.update({lines[i][-1]: {}})
        #print(lines[i][-1])
        print(currentPath)
    else:
        fileSize, fileName = lines[i].split(" ")
        currentPath[fileName] = fileSize


print(outermost)
