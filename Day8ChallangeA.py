with open('Day8ChallangeData', 'r') as file:
    inputFile = file.read()

lines = inputFile.split("\n")
grid = [[int(x) for x in line] for line in lines]
gridWidth = len(grid[0])
gridHeight = len(grid)

exteriorTrees = 2 * len(grid) + 2 * len(grid[0]) - 4
visibleInteriorTrees = 0

print("Grid:", grid)
print("Grid width:", gridWidth)
print("Grid height:", gridHeight)


def check_visibility(g, w, h):
    visibleFromWest = True
    visibleFromEast = True
    visibleFromNorth = True
    visibleFromSouth = True
    #print(g[w][h])
    treeHeight = g[w][h]
    #print(w, h)
    for x in range(0, w, 1):
        if g[x][h] < treeHeight:
            continue
        visibleFromWest = False
        break
    for x in range(w + 1, gridWidth, 1):
        if g[x][h] < treeHeight:
            continue
        visibleFromEast = False
        break
    for y in range(0, h, 1):
        if g[w][y] < treeHeight:
            continue
        visibleFromNorth = False
        break
    for y in range(h + 1, gridHeight, 1):
        if g[w][y] < treeHeight:
            continue
        visibleFromSouth = False
        break
    if visibleFromWest or visibleFromEast or visibleFromNorth or visibleFromSouth:
        return True
    else:
        return False


for w in range(1, gridWidth - 1, 1):
    for h in range(1, gridHeight - 1, 1):
        print(grid[w][h], check_visibility(grid, w, h))
        if check_visibility(grid, w, h):
            visibleInteriorTrees += 1

totalVisibleTrees = visibleInteriorTrees + exteriorTrees
print("Visible interior trees:", visibleInteriorTrees)
print("Exterior trees:", exteriorTrees)
print("Total visible trees:", totalVisibleTrees)