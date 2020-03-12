import logging
'''This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.'''

def firstMissingPositiveInt(myArray):
    ''' Method to return the first positive integer missing from an array'''
    myArray.sort()
    lowestFound = 1

    for i in myArray:
        if i >= 1:
            if i == lowestFound:
                lowestFound = lowestFound + 1
            elif i > lowestFound:
                return lowestFound

    return lowestFound
            


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    a = [3,4,-1,1]#2
    result = firstMissingPositiveInt(a)
    logging.debug(result)

    a=[1,1,1,1,2,4,0]#3
    result = firstMissingPositiveInt(a)
    logging.debug(result)