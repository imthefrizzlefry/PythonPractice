'''This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''

from random import random
radius = 2


def estimate_pi(num_random_tests):
    pi_counter = 0
    rsquared = radius ** 2
    for _ in range(num_random_tests):
        x_rand = random() * radius
        y_rand = random() * radius
        if (x_rand ** 2) + (y_rand ** 2) < rsquared:
            pi_counter += 1

    return 4 * pi_counter / num_random_tests

my_pi = estimate_pi(1000000000)
assert round(my_pi, 3) == 3.141