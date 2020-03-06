
def countingValleys(n, s):
    valleyCount = 0
    climb = 0

    for t in s:
        if t == 'D' and climb == 0:
            valleyCount += 1
        
        if t == 'D':
            climb += 1
        else:
            climb -= 1
            
    return valleyCount