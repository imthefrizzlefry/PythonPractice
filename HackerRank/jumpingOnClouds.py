def jumpingOnClouds(c):
    numberOfJumps = 0
    position = 0

    while position < len(c)-1:
        if position < len(c)-2 and c[position+2] == 0:
            position += 2
        else:
            position += 1
        numberOfJumps += 1

    return numberOfJumps