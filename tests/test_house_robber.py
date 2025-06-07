import pytest

from problems.house_robber import Solution


@pytest.mark.parametrize(
    "nums, expected", [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
    ]
)
def test(nums, expected):
    actual = Solution().rob(nums)

    assert actual == expected
