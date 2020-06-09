''' This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

https://en.wikipedia.org/wiki/Reservoir_sampling

'''

import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element



print(pick([5, 4, 6, 23, 88, 72, 100, 94, 22, 44, 66, 55]))
print(pick([7]))
print(pick([]))