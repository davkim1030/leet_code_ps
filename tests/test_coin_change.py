import pytest

from problems.coin_change import Solution


@pytest.mark.parametrize(
    "coins, amount, expected", [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ]
)
def test(coins, amount, expected):
    actual = Solution().coinChange(coins, amount)

    assert expected == actual
