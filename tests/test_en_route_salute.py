import pytest
from hamcrest import assert_that, equal_to

from src.en_route_salute import answer


@pytest.mark.parametrize("test_input,expected", [
    ('', 0),
    ('--', 0),
    ('--', 0),
    ('<>', 0),
    ('><', 2),
    ('<-->', 0),
    ('<<>>', 0),
    ('--<---<--->--><<<<<---', 20),
    ('<<>><<<>>>', 12),
    ('>><<<', 12),
    ('>', 0),
    ('->-------', 0),
    ('<', 0),
])
def test_simple(test_input, expected):
    assert_that(answer(test_input), equal_to(expected))
