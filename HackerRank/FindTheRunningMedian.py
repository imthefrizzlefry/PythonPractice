#!/bin/python3

import os
import sys
import heapq

def addNum(num, lowers, highers):
    if not lowers or num < -lowers[0]:
        heapq.heappush(lowers,-num)
    else:
        heapq.heappush(highers,num)
    
def rebalance(lowers, highers):
    if len(lowers) - len(highers) >= 2:
        heapq.heappush(highers,-heapq.heappop(lowers))
    elif len(highers) - len(lowers) >= 2:
        heapq.heappush(lowers,-heapq.heappop(highers))

def getMedian(lowers, highers):
    if len(lowers) == len(highers):
        return (-lowers[0] + highers[0])/2
    if len(lowers) > len(highers):
        return float(-lowers[0])
    else:
        return float(highers[0])


def runningMedian(a):
    lowers = []  # max heap, vals should go in and come out negated
    highers = []  # min heap, vals should go in positive
    result = []
    for v in a:
        addNum(v, lowers, highers)
        rebalance(lowers, highers)
        result.append(round(getMedian(lowers, highers),1))
    return result

#
# Complete the runningMedian function below.
#
# def runningMedian(a):
#     #
#     # Write your code here.
#     #
#     if len(a) < 2: return a
#     l = len(a)
#     segment = []
#     result = []

#     for i in range(l):
#         segment.append(a[i])
#         midpoint = len(segment)//2
#         segment.sort()
#         if len(segment)%2 == 0:
#             median = (segment[midpoint]+segment[midpoint-1])/2
#             result.append(median)
#         else:
#             result.append(segment[midpoint])

#     return result



if __name__ == '__main__':

    result = runningMedian([])
    print( '\n'.join(map(str, result)))
    result = runningMedian([12])
    print( '\n'.join(map(str, result)))
    result = runningMedian([12,4,5,3,8,7])
    print( '\n'.join(map(str, result)))

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # a_count = int(input())

    # a = []

    # for _ in range(a_count):
    #     a_item = int(input())
    #     a.append(a_item)

    # result = runningMedian(a)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()