import pytest

from problems.median_of_two_sorted_arrays import Solution


@pytest.mark.parametrize(
    "nums1, nums2, expected", [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([1], [], 1.0),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 9.0),
        ([], [1, 2, 3, 4], 2.5),
        ([1, 2, 3, 4], [], 2.5),
    ]
)
def test(nums1, nums2, expected: float):
    actual = Solution().findMedianSortedArrays(nums1, nums2)

    assert expected == actual
