from random import randint

import pytest
from hamcrest import assert_that, equal_to

from src.hey_i_already_did_that import answer, convert_to_base, next_minion_id


def test_base_conv():
    digits = list(convert_to_base(6, 2))
    assert_that(digits, equal_to([1, 1, 0]))
    print(convert_to_base(14, 9))


@pytest.mark.parametrize(('test_input', 'test_base', 'expected_value'), [
    (
            '210111',
            3,
            '122221'
    ),
    (
            '122221',
            3,
            '102212'
    ),
    (
            '102212',
            3,
            '210111'
    )
])
def test_algorithm(test_input, test_base, expected_value):
    assert_that(next_minion_id(test_input, test_base), equal_to(expected_value))


@pytest.mark.parametrize(('test_n', 'test_b', 'expected_value'), [
    (

            "1211",
            10,
            1
    ),
    (
            "210022",
            3,
            3
    ),
    (
            "423213",
            5,
            5
    ),
    (
            "320322",
            5,
            5
    ),
    (
            "0",
            5,
            1
    ),
    (
            "00",
            2,
            1
    ),
    (
            "00",
            2,
            1
    )
])
def test_simple(test_n, test_b, expected_value):
    assert_that(answer(test_n, test_b), equal_to(expected_value))


def test_random():
    for b in range(2, 10):
        for k in range(2, 9):
            for i in range(10):
                # just computes a few of each base-length possibility to make sure nothing blows up
                n = ''.join(map(str, [randint(0, b - 1) for _ in range(k)]))
                x = answer(n, b)
                print('{}, {}, {}'.format(n, int(n, base=b), x))