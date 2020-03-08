import logging

''' This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def arrayOfProducts(myArray):
    n = len(myArray)
    newArray = [0]*n
    prodBeforeI = [1]*n
    prodAfterI = [1]*n

    for i in range(1, n):
        prodBeforeI[i] = myArray[i-1] * prodBeforeI[i-1]
        prodAfterI[n-1-i] = myArray[n-i] * prodAfterI[n-i] 

    for i in range(0, n):
        newArray[i] = prodBeforeI[i] * prodAfterI[i]

    return newArray
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    a = [1,2,3,4,5]

    result = arrayOfProducts(a)
    logging.debug(result)