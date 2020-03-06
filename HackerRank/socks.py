import math
def sockMerchant(n, ar):
    myDict = {}
    numPairs = 0

    for s in ar:
        if s not in myDict:
            myDict[s] = 1
        else:
            myDict[s] += 1

    for p in myDict:
        numPairs += math.floor(myDict[p] / 2)


    return numPairs