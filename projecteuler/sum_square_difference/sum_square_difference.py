# Link: https://projecteuler.net/problem=6
def sum_square_difference():
    n = 100

    # Based off formula N(N+1)/2 to calculate sum of N consecutive terms starting from 1
    sum_of_first_n_terms = (n)*(n+1) / 2
    square_of_sum = sum_of_first_n_terms ** 2

    # Can prove by induction that 1^2 + .... + n^2 is n(n+1)(2n+1)/6. This can be rearranged
    # to use one of the previous calculations to avoid repeated calculations
    sum_of_squares = (sum_of_first_n_terms) * (2 * n + 1) / 3

    print(square_of_sum - sum_of_squares)


sum_square_difference()
