import pytest
from hamcrest import assert_that, equal_to

from src.distract_the_guards import answer


@pytest.mark.parametrize(('banana_list', 'expected_value'), [
    ([1, 1], 2),
    ([1, 7, 3, 21, 13, 19], 0),
    ([], 0)
])
def test_simple(banana_list, expected_value):
    assert_that(answer(banana_list), equal_to(expected_value))
