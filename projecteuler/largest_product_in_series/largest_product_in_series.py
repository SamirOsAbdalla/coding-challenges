

def get_largest_product():
    # I could have used a multiline string but I didn't want to have to check for newlines
    num_str = """7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"""

    str_len = len(num_str)

    num_adjacent = 13
    l, r = 0, -1

    max_product = 0

    # Need to find a suitable starting point. If we have a 0 in our current substr then
    # of course we need to find one without it since we start our max_product at 0
    cur_substr_len = 0
    while (cur_substr_len < num_adjacent):
        r += 1
        if (num_str[r] == "0"):
            cur_substr_len = 0
        else:
            cur_substr_len += 1

    # The resulting substr will not have any 0's in it
    l = r - (num_adjacent - 1)

    while (r < str_len):
        if (num_str[r] == "0" or num_str[l] == "0"):

            # Could probably put this in a function but it's not too much repeated code
            while (r < str_len and cur_substr_len < num_adjacent):
                r += 1
                cur_substr_len = 0
                if (num_str[r] == "0"):
                    cur_substr_len = 0
                else:
                    cur_substr_len += 1
            if (r == str_len):
                return
            l = r - (num_adjacent - 1)

        # Now we just need to extract the current substring and loop over its individual integers
        substr = num_str[l: r + 1]
        cur_product = 1
        for c in substr:
            cur_product *= int(c)
        if (cur_product > max_product):
            max_product = cur_product
        r += 1
        l += 1

    print(max_product)


get_largest_product()
