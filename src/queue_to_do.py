def cum_xor_of_line(first, last):
    """
    calculates the cumulative xor for a consecutive range of integers from first (inclusive) to last (inclusive)
    >>> cum_xor_of_line(1, 3) == 1 ^ 2 ^ 3
    :param first: the first integer in the range (inclusive)
    :param last: the last integer in the range (inclusive)
    :return: the cumulative xor value
    """
    # a quick throw for an invalid value
    if first > last:
        raise ValueError('first must be less than or equal to last, and both must be integers')

    # a quick guard for a single value
    if first == last:
        return first

    # work out some variables
    is_first_even = first % 2 == 0
    is_last_odd = last % 2 != 0

    # we're going to use a shortcut here rather than actually compute the cumulative xor value iteratively
    # the basis behind this is a few truths about the exclusive or operation
    # 1) an even-odd pair of consecutive numbers xor'ed will always result in 1. eg ( 4 ^ 5 = 1 ) or ( 16 ^ 17 = 1 )
    # 2) 1 xor 1 equals 0, meaning a pair of even-odd pairs equals 0, eg ( 2 ^ 3 ^ 4 ^ 5 == 1 ^ 1 == 0 )
    # 3) anything xor'ed with 0, equals itself. eg ( 45 ^ 0 = 45 )

    # first we work out if there's an even number of even-odd pairs.
    # eg. given (1, 2, 3, 4, 5) the first even number is 2, and the last odd number is 5
    # then we work out the range of those numbers and divide by 2 to get the number of pairs.
    # then we just check if that number is even
    first_even_num = first if is_first_even else first + 1
    last_odd_number = last if is_last_odd else last - 1
    has_even_number_of_pairs = ((last_odd_number + 1 - first_even_num) / 2) % 2 == 0

    # using these rules, we can just replace any amount of even-odd pairs in the number range with
    # either a 0 or a 1. 0 if there's an even amount of pairs, 1 if there's an odd amount of pairs.
    # where by 'pair' I actually mean pair of even-off pairs! Oh boy.
    collapsed_xor_value = 0 if has_even_number_of_pairs else 1
    # finally we just cover all 4 possibilities for whether the start, end, or neither
    # were included in the collapsed portion of the range.
    # I think this reads better than using ternaries to compute the start and end portions.. despite not being as terse
    if is_first_even and not is_last_odd:
        return collapsed_xor_value ^ last
    elif not is_first_even and not is_last_odd:
        return first ^ collapsed_xor_value ^ last
    elif is_first_even and is_last_odd:
        return collapsed_xor_value
    elif not is_first_even and is_last_odd:
        return first ^ collapsed_xor_value


def answer(start, length):
    checksum = 0
    # we know the total number of lines we're going to check is equal to the length of the first line
    for i in xrange(length):
        # we can quickly work out the start and end (inclusive) integers of each line
        start_of_line = start + i * length
        end_of_line = start_of_line + length - i - 1
        # then we can work out the cumulative xor value for the entire line
        # and add that to our checksum with the xor operator
        checksum ^= cum_xor_of_line(start_of_line, end_of_line)
    # boom!
    return checksum
