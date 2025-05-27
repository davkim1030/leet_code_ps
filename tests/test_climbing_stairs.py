import pytest

from problems.climbing_stairs import Solution


@pytest.mark.parametrize(
    "n, expected", [
        (2, 2),
        (3, 3),
    ]
)
def test(n, expected):
    actual = Solution().climbStairs(n)

    assert expected == actual
