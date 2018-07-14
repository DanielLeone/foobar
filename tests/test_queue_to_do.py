import operator

import pytest
from hamcrest import assert_that, equal_to

from src.queue_to_do import answer, cum_xor_of_line


def xor(line):
    return reduce(operator.xor, line, 0)


@pytest.mark.parametrize('input', [
    ([0, 1, 2, 3]),
    ([1, 2, 3]),
    ([1]),
    ([1, 2, 3]),
    ([1, 2, 3, 4, 5, 6]),
    ([2, 3, 4, 5, 6]),
    ([2, 3, 4, 5]),
    ([12, 13, 14, 15]),
    ([13, 14, 15, 16]),
    ([13, 14, 15, 16, 17]),
    ([13, 14, 15, 16, 17, 18, 19, 20]),
    ([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]),
    ([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]),
    ([17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),
    ([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]),
    ([6, 7, 8, 9, 10, 11]),
    ([6, 7, 8, 9, 10, 11, 12, 13]),
    ([8, 9, 10, 11, 12, 13, 14, 15, 16, 17]),
])
def test_xor_of_line(input):
    assert_that(cum_xor_of_line(input[0], input[-1]), equal_to(xor(input)))


@pytest.mark.parametrize(('start', 'length', 'expected_value'), [
    (0, 3, 2),
    (17, 4, 14),
    (0, 10, 19),
    (1, 10, 64),
])
def test_simple(start, length, expected_value):
    assert_that(answer(start, length), equal_to(expected_value))
