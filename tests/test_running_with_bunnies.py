import pytest
from hamcrest import assert_that, equal_to

from src.running_with_bunnies import all_permutations, answer, has_negative_cycle


@pytest.mark.parametrize(('times', 'time_limit', 'expected_value'), [
    (
            [
                [0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0]
            ],
            3,
            [0, 1]
    ),
    (
            [
                [0, 2, 2, 2, -1],
                [9, 0, 2, 2, -1],
                [9, 3, 0, 2, -1],
                [9, 3, 2, 0, -1],
                [9, 3, 2, 2, 0]
            ],
            1,
            [1, 2]
    ),
    (
            [
                [0, 2, 2, 2, -1],
                [9, 0, 2, 2, 0],
                [9, 3, 0, 2, 0],
                [9, 3, 2, 0, 0],
                [-1, 3, 2, 2, 0]
            ],
            -500,
            [0, 1, 2]
    ),
    (
            [
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1]
            ],
            1,
            []
    ),
    (
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ],
            2,
            [0]
    ),
    (
            [
                [0, 5, 11, 11, 1],
                [10, 0, 1, 5, 1],
                [10, 1, 0, 4, 0],
                [10, 1, 5, 0, 1],
                [10, 10, 10, 10, 0]
            ],
            10,
            [0, 1]
    ),
    (
            [
                [0, 10, 10, 10, 1],
                [0, 0, 10, 10, 10],
                [0, 10, 0, 10, 10],
                [0, 10, 10, 0, 10],
                [1, 1, 1, 1, 0]
            ],
            5,
            [0, 1]
    ),
    (
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ],
            1,
            [0, 1, 2]
    ),
    (
            [
                [2, 2],
                [2, 2]
            ],
            1,
            []
    ),
    (
            [
                [0, 10, 10, 1, 10],
                [10, 0, 10, 10, 1],
                [10, 1, 0, 10, 10],
                [10, 10, 1, 0, 10],
                [1, 10, 10, 10, 0]
            ],
            6,
            sorted([2, 1, 0])

    )
])
def test_simple(times, time_limit, expected_value):
    assert_that(answer(times, time_limit), equal_to(expected_value))


@pytest.mark.parametrize(('graph', 'has_cycle'), [
    (
            [
                [0, -2, 3],
                [1, 0, 3],
                [3, 3, 0],
            ],
            True
    ),
    (
            [
                [0, 3, 3],
                [3, 0, 3],
                [3, 3, 0],
            ],
            False
    ),
    (
            [
                [0, 2, 0, 3, 4],
                [-3, 0, 2, 2, 2],
                [2, 2, 0, 1, 2],
                [2, 1, 2, 0, 2],
                [2, 2, 2, 2, 0],
            ],
            True
    ),
    (
            [
                [0, 0],
                [0, 0]
            ],
            False
    )
])
def test_negative_cycle(graph, has_cycle):
    assert_that(has_negative_cycle(graph), equal_to(has_cycle))


@pytest.mark.parametrize(('items', 'permutations'), [
    (
            [1],
            [
                (1,),
                (),
            ]
    ),
    (
            [1, 2],
            [
                (1, 2),
                (2, 1),
                (1,),
                (2,),
                (),
            ]
    ),
    (
            [1, 2, 3],
            [
                (1, 2, 3),
                (1, 3, 2),
                (2, 1, 3),
                (2, 3, 1),
                (3, 1, 2),
                (3, 2, 1),
                (1, 2),
                (1, 3),
                (2, 1),
                (2, 3),
                (3, 1),
                (3, 2),
                (1,),
                (2,),
                (3,),
                (),
            ]
    )
])
def test_permutations(items, permutations):
    assert_that(all_permutations(items), equal_to(permutations))
