import pytest
from hamcrest import assert_that, equal_to

from src.dodge_the_lasers import answer


@pytest.mark.parametrize(('n', 'expected_value'), [
    ('5', '19'),
    ('77', '4208')
])
def test_simple(n, expected_value):
    assert_that(answer(n), equal_to(expected_value))
