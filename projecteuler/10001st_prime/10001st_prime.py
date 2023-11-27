# Link: https://projecteuler.net/problem=7
import math


def is_prime(n):

    # only need to check until sqrt(n) since if n were not prime we would have
    # found the other factor
    upper_bound = math.floor(math.sqrt(n))
    for i in range(2, upper_bound+1, 1):
        if (n % i == 0):
            return False
    return True


def get_specified_prime():
    specified_prime = 10001

    # going to start at 3 for simplicity
    num_primes = 2
    i = 4
    while (True):
        if (is_prime(i)):
            num_primes += 1
            if (num_primes == specified_prime):
                print(i)
                return
        i += 1


get_specified_prime()
