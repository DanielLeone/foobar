def answer(l):
    # this will store our total count of triples
    total_count_of_triples = 0
    # this will store the count of found divisors for each item,
    # referenced by the same index. So if l = [1,2,3] we'd expect [0, 1, 1]
    # as 2 has 1 divisor (1) and 3 has 1 divisor (1)
    count_doubles_for_index = []
    # go through each item in the list
    for i, item in enumerate(l):
        # always start the count at 0 here, so we don't get an IndexError later
        count_doubles_for_index.append(0)
        # for each item, go through all the previous items again
        for j in range(i):
            other = l[j]
            # if we find a valid divisor (we use a float cast to make sure we don't get stung by integer division)
            if item % float(other) == 0:
                # increase our count of divisors by 1 for the current item (ie, the number of doubles found)
                count_doubles_for_index[i] += 1
                # and increase out total count of triples by the amount of divisors for the the other item
                # ..this is where the magic happens..
                # if we find a valid double pair. eg. (4, 8)
                # we just have to find out how many doubles we've already got for 4. eg (2, 4) and (1, 4)
                # and that would make our lucky triple. eg (2, 4, 8) and (1, 4, 8)
                total_count_of_triples += count_doubles_for_index[j]
    return total_count_of_triples
