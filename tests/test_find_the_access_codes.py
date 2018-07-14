import pytest
from hamcrest import assert_that, equal_to

from src.find_the_access_codes import answer


@pytest.mark.parametrize(('test_l', 'expected_value'), [
    ([1], 0),
    ([1, 1], 0),
    ([1, 1, 1], 1),
    ([1, 1, 1, 1], 4),
    ([1, 2, 3, 4, 5, 6], 3),
    ([1, 2, 3], 0),
    ([1, 2, 4], 1),
    ([1, 8, 8], 1),
])
def test_simple(test_l, expected_value):
    assert_that(answer(test_l), equal_to(expected_value))
