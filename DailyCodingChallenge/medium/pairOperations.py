import logging
'''This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 

For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons on line 10

Implement car and cdr.
'''
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def left(a, b):
        return a
    return pair(left)

def cdr(pair):
    def right(a, b):
        return b
    return pair(right)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    a = 3
    b = 4

    logging.debug(cons(a,b))

    # expect 3
    logging.debug(car(cons(a,b)))

    # expect 4
    logging.debug(cdr(cons(a,b)))
