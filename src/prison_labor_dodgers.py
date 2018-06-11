def answer(x, y):
    # python sets for the winn! :D

    # turn both lists into sets
    # then just grab the symmetric difference of the sets
    # this should give us back another set with one item in it
    # so pop that and return it
    # return (set(x) ^ set(y)).pop()

    symmetric_difference = (set(x) ^ set(y))
    if len(symmetric_difference) != 1:
        raise Exception('doh')
    return symmetric_difference.pop()
