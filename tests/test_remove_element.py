import pytest

from problems.remove_element import Solution


@pytest.mark.parametrize(
    "nums, val, expected", [
        ([2, 3, 3, 2], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 4, 0, 3]),
    ]
)
def test(nums, val, expected):
    result = Solution().removeElement(nums, val)
    actual = nums[:result]

    assert expected == actual
