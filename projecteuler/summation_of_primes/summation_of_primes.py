# Link: https://projecteuler.net/problem=10
import math


def is_prime(i):
    sqrt_i = math.floor(math.sqrt(i))
    for n in range(2, sqrt_i + 1):
        if (i % n == 0):
            return False
    return True


def summation_of_primes():
    max_val = 2_000_000

    # Just going to start at 4 for loop simplicity
    cur_sum = 5

    for i in range(4, max_val):
        if (is_prime(i)):
            cur_sum += i
    print(cur_sum)


summation_of_primes()
