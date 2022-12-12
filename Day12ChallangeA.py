# Read data and generate grid
with open('Day12ChallangeData') as f:
    lines = f.readlines()
lines = [line.rstrip() for line in lines]
grid = []
for line in lines:
    grid.append(list(line))


# Init path, lowest path steps, number of finished recursions
initPath = []
pathSteps = [250]
createdRecursions = 0
finishedRecursions = 0
topX = [0]
topXDif = 23

# Convert to integer
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            grid[i][j] = 0
            continue
        elif grid[i][j] == 'E':
            grid[i][j] = 27
            continue
        grid[i][j] = ord(grid[i][j]) - 96


def move_possible(target_coord, height):
    if 0 <= target_coord['y'] <= len(grid) - 1 and 0 <= target_coord['x'] <= len(grid[0]) - 1 and \
            grid[target_coord['y']][target_coord['x']] - height <= 1:
        #print(grid[target_coord['y']][target_coord['x']], height, grid[target_coord['y']][target_coord['x']] - height)
        return True
    return False


# Move to new position
def visit(current_coord, path):
    #print("Visit körs, steps:", len(path))
    path.append(current_coord)
    #topX.append(current_coord['x'])
    #print(current_coord['x'])
    global createdRecursions
    if grid[current_coord['y']][current_coord['x']] == 27:
        print("- - - Path found. Steps: ", len(path) - 1, "- - -")
        pathSteps.append(len(path) - 1)
    elif len(path) < min(pathSteps):
        height = grid[current_coord['y']][current_coord['x']]
        right = {'y': current_coord['y'], 'x': current_coord['x'] + 1}
        left = {'y': current_coord['y'], 'x': current_coord['x'] - 1}
        up = {'y': current_coord['y'] - 1, 'x': current_coord['x']}
        down = {'y': current_coord['y'] + 1, 'x': current_coord['x']}

        if move_possible(right, height) and right not in path:
            #print("possible right jao")
            createdRecursions += 1
            visit(right, path.copy())

        if move_possible(left, height) and left not in path:
            #print("possible left jao")
            createdRecursions += 1
            visit(left, path.copy())

        if move_possible(up, height) and up not in path:
            #print("possible up jao")
            createdRecursions += 1
            visit(up, path.copy())

        if move_possible(down, height) and down not in path:
            #print("possible down jao")
            createdRecursions += 1
            visit(down, path.copy())
    else:
        global finishedRecursions
        finishedRecursions += 1
        #print(finishedRecursions, createdRecursions, createdRecursions - finishedRecursions)



# Print grid with zero-padding
for row in grid:
    formatted_numbers = [str(n).zfill(2) for n in row]
    print(formatted_numbers)

visit({'y': 20, 'x': 0}, initPath)
print(min(pathSteps))
