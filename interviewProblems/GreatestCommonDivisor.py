'''  Demo question from Amazon Demo Assessment

Given an array arr of given length num, find the greatest common divisor that goes into every number of the array.

the num parameter is kind of useless in python.  but you can use it rather than calling len(arr)...
'''

def generalizedGCD(num, arr):
    div = arr[0]

    for i in range(1, num):
        div = gcd(div,arr[i])
        if div == 1:
            return 1
    return div

def gcd(x, y): # Euclidean method...
        while y:
            x,y = y,x%y
        return x


print(generalizedGCD(5,[2,4,6,8,10])) # prints 2

print(generalizedGCD(5,[2,4,6,8,10])) # prints 1