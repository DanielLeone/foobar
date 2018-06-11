def digits_to_str(digits):
    # just turns a list of integers into a single string
    return ''.join(map(str, digits))


def convert_to_base(n, b):
    # turns an integer into a list of digits for the forgiven base
    # for example converting 6 in base 10, into base 2
    # 6 % 2 ~= 0, so we put a 0, [0], then divide 6 by 2 ~= 3
    # 3 % 2 ~= 1, so in our base 2 digits we put a 1, [1, 0], then divide 3 by 2 ~= 1
    # 1 % 2 ~= 1, so in our base 2 digits we put a 1, [1, 1, 0], then divide 1 by 2 ~= 0
    # we reached 0 with [1, 1, 0] -- which is 6 in base 2!
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.insert(0, int(n % b))
        n /= b
    return digits


def next_minion_id(n, b):
    k = len(n)

    # take n as digits and sort them in both directions
    digits_desc = sorted(map(int, n))
    digits_asc = reversed(digits_desc)

    # parse those back into integers keeping track of their base
    x = int(digits_to_str(digits_asc), base=b)
    y = int(digits_to_str(digits_desc), base=b)

    # calculate z and convert it into the correct base
    z = x - y
    z_in_base_b = digits_to_str(convert_to_base(z, b))

    # then left pad it with zeros and return it
    return z_in_base_b.zfill(k)


def answer(n, b):
    """
    But seriously, who stores IDs in different bases :P
    I thought I was going about this challenge the wrong way by actually implementing the algorithm that was described.
    I spent a while looking at all the results, convinced there was a pattern somewhere I was meant to find.
    Maybe there still is... eh, it was fun at least :)
    Cheers!
    """
    i = 0
    seen_values = {}
    # mmm a nice litle infinite loop
    while True:
        # if we've already seen this minion ID, we've hit the end of a loop!
        if n in seen_values:
            # return the difference between the iteration we're at now
            # and the iteration the loop started at
            return i - seen_values[n]
        # otherwise keep track of this ID and the current iteration
        seen_values[n] = i
        i += 1
        # calculate the next ID
        n = next_minion_id(n, b)
