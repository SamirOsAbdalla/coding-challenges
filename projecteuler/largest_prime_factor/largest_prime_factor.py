value = 600851475143


def calculate_largest_prime_factors(num):
    cur_factors = []
    divisor = 2

    # Continuously divide num until we reach 1. We are guaranteed to reach 1 since
    # we will eventually divide the num by itself if no other factors are found
    while (num > 1):
        if (num % divisor == 0):
            cur_factors.append(divisor)
            num /= divisor
        divisor += 1
    return max(cur_factors)


print(calculate_largest_prime_factors(value))
