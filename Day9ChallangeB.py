with open('Day9ChallangeData', 'r') as file:
    lines = file.readlines()
lines = [item.strip() for item in lines]


tailComponents = [
    {
        'x': 0,
        'y': 0,
        'touchedPositions': ["x0 y0"]
    },
    {
        'x': 0,
        'y': 0,
        'touchedPositions': ["x0 y0"]
    },
    {
        'x': 0,
        'y': 0,
        'touchedPositions': ["x0 y0"]
    },
    {
        'x': 0,
        'y': 0,
        'touchedPositions': ["x0 y0"]
    },
    {
        'x': 0,
        'y': 0,
        'touchedPositions': ["x0 y0"]
    },
    {
        'x': 0,
        'y': 0,
        'touchedPositions': ["x0 y0"]
    },
    {
        'x': 0,
        'y': 0,
        'touchedPositions': ["x0 y0"]
    },
    {
        'x': 0,
        'y': 0,
        'touchedPositions': ["x0 y0"]
    },
    {
        'x': 0,
        'y': 0,
        'touchedPositions': ["x0 y0"]
    },
    {
        'x': 0,
        'y': 0,
        'touchedPositions': ["x0 y0"]
    }
]


def move_head(d, s):
    print("Dags att flytta huvud jao")
    if d == 'L':
        for a in range(s):
            tailComponents[0]['x'] -= 1
            update_tail_position()
    elif d == 'R':
        for a in range(s):
            tailComponents[0]['x'] += 1
            update_tail_position()
    elif d == 'U':
        for a in range(s):
            tailComponents[0]['y'] -= 1
            update_tail_position()
    elif d == 'D':
        for a in range(s):
            tailComponents[0]['y'] += 1
            update_tail_position()
    print("\n")


def update_tail_position():
    for b in range(1, len(tailComponents), 1):
        frontComponent = tailComponents[b - 1]
        backComponent = tailComponents[b]
        if abs(backComponent['x'] - frontComponent['x']) > 1 or abs(backComponent['y'] - frontComponent['y']) > 1:
            if backComponent['x'] < frontComponent['x']:
                backComponent['x'] += 1
                if backComponent['y'] < frontComponent['y']:
                    backComponent['y'] += 1
                elif backComponent['y'] > frontComponent['y']:
                    backComponent['y'] -= 1
            elif backComponent['x'] > frontComponent['x']:
                backComponent['x'] -= 1
                if backComponent['y'] < frontComponent['y']:
                    backComponent['y'] += 1
                elif backComponent['y'] > frontComponent['y']:
                    backComponent['y'] -= 1
            elif backComponent['y'] < frontComponent['y']:
                    backComponent['y'] += 1
            elif backComponent['y'] > frontComponent['y']:
                    backComponent['y'] -= 1

        tailComponents[b - 1] = frontComponent
        tailComponents[b] = backComponent
        searchString = "x" + str(tailComponents[b]['x']) + " y" + str(tailComponents[b]['y'])
        print(searchString)
        if searchString not in tailComponents[b]['touchedPositions']:
            tailComponents[b]['touchedPositions'].append(searchString)


for line in lines:
    #print(line)
    direction, steps = line.split(" ")
    steps = int(steps)
    #print("Direction:", direction, "Steps:", steps)
    move_head(direction, steps)

print(len(tailComponents[9]['touchedPositions']))
