# Link: https://projecteuler.net/problem=4
import math


def isPalindrome(n):
    str_n = str(n)
    if (str_n == str_n[::-1]):
        return True
    return False


# Not happy with the time complexity but it is a simple brute forced solution
def largest_palindrome_product():
    max_palindrome = 0

    for i in range(100, 1000, 1):
        for j in range(100, 1000, 1):
            product = i * j
            if (isPalindrome(product) and product > max_palindrome):
                max_palindrome = product

    print(max_palindrome)


largest_palindrome_product()
