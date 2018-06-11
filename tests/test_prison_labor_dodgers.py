import pytest
from hamcrest import assert_that, calling, equal_to, raises

from src.prison_labor_dodgers import answer


@pytest.mark.parametrize(('test_x', 'test_y', 'expected_value'), [
    (
            [1, 2, 3],
            [1, 3],
            2
    ),
    (
            [1, 2],
            [1],
            2
    ),
    (
            [-3, -5, -8, -1, -2],
            [-3, -5, -8, -4, -1, -2],
            -4
    ),
])
def test_simple(test_x, test_y, expected_value):
    assert_that(answer(test_x, test_y), equal_to(expected_value))


def test_should_raise_if_empty():
    x = []
    y = []

    assert_that(calling(answer).with_args(x, y), raises(Exception, 'doh'))


def test_should_raise_if_not_found():
    x = [1, 2, 3]
    y = [1, 2, 3]

    assert_that(calling(answer).with_args(x, y), raises(Exception, 'doh'))
