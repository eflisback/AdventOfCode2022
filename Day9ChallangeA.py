with open('Day9ChallangeData', 'r') as file:
    lines = file.readlines()
lines = [item.strip() for item in lines]

head = {
    'x': 0,
    'y': 0#,
    #'touchedPositions': ["x0 y0"]
}
tail = {
    'x': 0,
    'y': 0,
    'touchedPositions': ["x0 y0"]
}


def move_head(d, s):
    print("Dags att flytta huvud jao")
    if d == 'L':
        for a in range(s):
            initHeadPosition = {'x': head['x'], 'y': head['y']}
            head['x'] -= 1
            update_tail_position(initHeadPosition)
    elif d == 'R':
        for a in range(s):
            initHeadPosition = {'x': head['x'], 'y': head['y']}
            head['x'] += 1
            update_tail_position(initHeadPosition)
    elif d == 'U':
        for a in range(s):
            initHeadPosition = {'x': head['x'], 'y': head['y']}
            head['y'] -= 1
            update_tail_position(initHeadPosition)
    elif d == 'D':
        for a in range(s):
            initHeadPosition = {'x': head['x'], 'y': head['y']}
            head['y'] += 1
            update_tail_position(initHeadPosition)
    print("\n")


def update_tail_position(targetPos):
    if abs(tail['x'] - head['x']) > 1 or abs(tail['y'] - head['y']) > 1:
        tail['x'] = targetPos['x']
        tail['y'] = targetPos['y']
        searchString = "x" + str(tail['x']) + " y" + str(tail['y'])
        print(searchString)
        if searchString not in tail['touchedPositions']:
            tail['touchedPositions'].append(searchString)


for line in lines:
    #print(line)
    direction, steps = line.split(" ")
    steps = int(steps)
    #print("Direction:", direction, "Steps:", steps)
    move_head(direction, steps)

print(head)
print(len(tail['touchedPositions']))
