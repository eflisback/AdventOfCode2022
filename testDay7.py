with open('Day7ChallangeData', 'r') as file:
    lines = file.readlines()

totalSize = 100000
directorySizes = []

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    if "ls" in lines[i]:
        a = 1
        dirSize = 0
        while True:
            if lines[i + a][0] == '$':
                break
            elif "dir" not in lines[i + a]:
                fileSize, fileName = lines[i + a].split(" ")
                dirSize += int(fileSize)
            a += 1
        if dirSize < totalSize:
            directorySizes.append(dirSize)
        print("Done with loop. dirSize =", dirSize)

print(sum(directorySizes))