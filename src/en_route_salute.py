def answer(s):
    """
    calculates the total number of salutes
    that will occur in a given hallway.
    """
    number_of_passed_right_movers = 0
    number_of_salutes = 0
    # we iterate over each character of the string moving from LEFT to RIGHT
    for char in s:
        if char == '<':
            # if we pass someone going left
            # we add 2 salutes (1 for each person) for every person in there path who is going right
            number_of_salutes += 2 * number_of_passed_right_movers
        elif char == '>':
            # if we see someone going right, keep track on them,
            # because someone who is going left in front of us will eventually run into them
            number_of_passed_right_movers += 1
    return number_of_salutes
