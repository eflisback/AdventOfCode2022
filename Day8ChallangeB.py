with open('Day8ChallangeData', 'r') as file:
    inputFile = file.read()

lines = inputFile.split("\n")
grid = [[int(x) for x in line] for line in lines]
gridWidth = len(grid[0])
gridHeight = len(grid)

exteriorTrees = 2 * len(grid) + 2 * len(grid[0]) - 4
visibleInteriorTrees = 0
scores = []

print("Grid:", grid)
print("Grid width:", gridWidth)
print("Grid height:", gridHeight)


def check_visibility(g, y, x):
    scoreToWest = 0
    scoreToEast = 0
    scoreToNorth = 0
    scoreToSouth = 0
    westViwed = False
    eastViewed = False
    northViewed = False
    southViewed = False
    treeHeight = g[y][x]

    for i in range(x + 1, len(g[y]), 1):
        if eastViewed:
            continue
        if g[y][i] >= treeHeight:
            eastViewed = True
        scoreToEast += 1
    for i in range(x - 1, -1, -1):
        if westViwed:
            continue
        if g[y][i] >= treeHeight:
            westViwed = True
        scoreToWest += 1
    for i in range(y - 1, -1, -1):
        if northViewed:
            continue
        if g[i][x] >= treeHeight:
            northViewed = True
        scoreToNorth += 1
    for i in range(y + 1, len(grid), 1):
        if southViewed:
            continue
        if g[i][x] >= treeHeight:
            southViewed = True
        scoreToSouth += 1

    return scoreToWest * scoreToEast * scoreToNorth * scoreToSouth


for w in range(1, gridWidth - 1, 1):
    for h in range(1, gridHeight - 1, 1):
        scores.append(check_visibility(grid, h, w))


print(max(scores))
