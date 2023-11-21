a0 = 1
a1 = 1

sum = 0
while (a1 < 4000000):
    a2 = a0 + a1
    if (a2 % 2 == 0):
        sum += a2
    a0 = a1
    a1 = a2

print(sum)
