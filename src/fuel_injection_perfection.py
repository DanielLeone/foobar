def answer(n):
    """
    Calculates the minimum number of steps needed to reduce n to 1,
    when available operations are to add 1, subtract 1 or divide by 2 when n is even.

    Not the first time I'd come across bit masks,
    but definitely the first time I've actually had to use them :D
    Not gonna lie though, this still mostly came from StackOverflow,
    unfortunately you can't un-see the answer once you've already seen it.
    :type n: str
    :return: the number of steps taken to reduce n to 1
    """
    if not isinstance(n, basestring):
        raise TypeError('n must be a string')

    # huh.. today I learned that python integers are unbounded (meaning this shouldn't explode for that huge number)
    n = int(n)
    if n < 1:
        raise ValueError('n must be a positive integer as a string')
    count = 0
    while n > 1:
        count += 1
        if n % 2 == 0:
            # bit mask: (*0)
            # when even, dividing by 2 is always the best option
            n = n // 2
        elif n == 3 or n % 4 == 1:
            # bit mask: (*01)
            # or n is 3 (edge case that want to subtract at)
            n = n - 1
        else:
            # bit mask: (*11)
            # in this case it's best to add 1 because it will allow dividing for at least the next 2 steps.
            # Adding 1 to a number whose least significant bits are (*11) will always produce (*00).
            # Diving by 2 is equivalent to a single right shift of the bits,
            # meaning dividing (*00) by 2 gives us (*0), which we can right shift again to get (*)

            # a quick example
            # 7             = 00000111
            # 7 + 1 = 8     = 00001000  -- choosing to + 1 here
            # 8 >> 1 = 4    = 00000100  -- allowing right bit shift
            # 4 >> 1 = 2    = 00000010  -- and another!

            # and choosing the wrong path...
            # 7             = 00000111
            # 7 - 1 = 6     = 00000110  -- choosing to incorrectly subtract 1 here
            # 6 >> 1 = 3    = 00000011  -- allows only a single divide by 2, now the number is odd
            n = n + 1
    return count
