import pytest

from problems.minimum_size_subarray_sum import Solution


@pytest.mark.parametrize(
    "target, nums, expected", [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0)
    ]
)
def test(target, nums, expected):
    actual = Solution().minSubArrayLen(target, nums)

    assert expected == actual
