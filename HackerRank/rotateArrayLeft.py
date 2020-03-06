def rotLeft(a, d):
    finalArray = []

    if d == len(a):
        return a

    for x in range(d, len(a)):
        finalArray.append(a[x])
    
    for x in range(d):
        finalArray.append(a[x])
    
    return finalArray