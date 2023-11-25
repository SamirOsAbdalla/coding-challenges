# Link: https://projecteuler.net/problem=5


# Here is a brute force solution. I found a much better solution that
# increments by 2520 which makes sense considering the number has to
# be divisble from 1,...,10 and thus has to be a multiple of 2520. When
# incrementing by 2520 you would then only have to check from 20,...,11.
# Very smart and very efficient!
def smallest_multiple():
    upper_num = 20
    upper_range_num = upper_num + 1
    cur_num = 1
    while (True):
        if not cur_num % 2 == 0:
            pass
        else:
            for i in range(upper_num, 0, -1):
                if not (cur_num % i == 0):
                    break
                if (i == 1):
                    return cur_num
        cur_num += 1


print(smallest_multiple())
