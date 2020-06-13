

def get_prime_factors(num):
    factors = []
    divisor = 2
    while(divisor <= num):
        if (num % divisor) == 0:
            factors.append(divisor)
            num = num/divisor
        else:
            divisor += 1

    return factors


if __name__ == "__main__":
    inputs = [
        (13,[13]),
        (60,[2,2,3,5]),
        (630,[2,3,3,5,7])
    ]

    for pair in inputs:
        number = pair[0]
        expected_factors = pair[1]


        actual_factors = get_prime_factors(number)

        print("{} => {}".format(number, actual_factors))
        assert actual_factors == expected_factors