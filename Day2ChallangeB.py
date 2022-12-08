f = open("Day2ChallangeData", "r")
lines = f.readlines()

player1Points = 0
player2Points = 0


for i in range(len(lines)):
    row = lines[i]
    player1Char = row[0]
    player2Char = row[2]

    if player2Char == 'Z':
        if player1Char == 'A':
            player2Char = 'Y'
        elif player1Char == 'B':
            player2Char = 'Z'
        elif player1Char == 'C':
            player2Char = 'X'
    elif player2Char == 'Y':
        if player1Char == 'A':
            player2Char = 'X'
        elif player1Char == 'B':
            player2Char = 'Y'
        elif player1Char == 'C':
            player2Char = 'Z'
    elif player2Char == 'X':
        if player1Char == 'A':
            player2Char = 'Z'
        elif player1Char == 'B':
            player2Char = 'X'
        elif player1Char == 'C':
            player2Char = 'Y'

    if player1Char == 'A' and player2Char == 'X' or player1Char == 'B' and player2Char == 'Y' or player1Char == 'C' \
            and player2Char == 'Z':
        player1Points += 3
        player2Points += 3
    elif player1Char == 'A' and player2Char == 'Z' or player1Char == 'B' and player2Char == 'X' \
            or player1Char == 'C' and player2Char == 'Y':
        player1Points += 6
    elif player2Char == 'X' and player1Char == 'C' or player2Char == 'Y' and player1Char == 'A' \
            or player2Char == 'Z' and player1Char == 'B':
        player2Points += 6

    if player1Char == 'A':
        player1Points += 1
    elif player1Char == 'B':
        player1Points += 2
    elif player1Char == 'C':
        player1Points += 3

    if player2Char == 'X':
        player2Points += 1
    elif player2Char == 'Y':
        player2Points += 2
    elif player2Char == 'Z':
        player2Points += 3

print('P1: ', player1Points)
print('P2: ', player2Points)