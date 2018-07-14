import pytest
from hamcrest import assert_that, calling, equal_to, raises

from src.fuel_injection_perfection import answer


@pytest.mark.parametrize(('test_x', 'expected_value'), [
    ("1", 0),
    ("2", 1),
    ("3", 2),
    ("4", 2),
    ("5", 3),
    ("6", 3),
    ("7", 4),
    ("8", 3),
    ("9", 4),
    ("10", 4),
    ("15", 5),
    ("9" * 309, 1278),
    ("5" * 312, 1375)
])
def test_simple(test_x, expected_value):
    assert_that(answer(test_x), equal_to(expected_value))


def test_raises():
    assert_that(calling(answer).with_args("-1"), raises(ValueError))
    assert_that(calling(answer).with_args(1), raises(TypeError))
