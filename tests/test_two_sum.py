import pytest

from problems.two_sum import Solution


@pytest.mark.parametrize(
    "nums, target, expected", [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([15, 11, 7, 2], 9, [2, 3]),
        ([[3, 2, 4], 6, [1, 2]]),
        ([3, 3], 6, [0, 1]),
    ]
)
def test(nums, target, expected):
    actual = Solution().twoSum(nums, target)

    assert expected == actual
