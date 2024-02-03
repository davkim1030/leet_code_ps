from unittest import TestCase

from problems.median_of_two_sorted_arrays import Solution
from tests import PSTestCase


class TestMedianOfTwoSortedArrays(TestCase, PSTestCase):
    def setUp(self):
        self.solution_class = Solution()
    def solution(self, *args, **kwargs) -> any:
        return self.solution_class.findMedianSortedArrays(*args, **kwargs)

    def test(self):
        # Given
        nums1 = [1, 3]
        nums2 = [2]

        # When
        result = self.solution(nums1, nums2)

        # Then
        self.assertEqual(result, 2.0)

    def test2(self):
        # Given
        nums1 = [1, 2]
        nums2 = [3, 4]

        # When
        result = self.solution(nums1, nums2)

        # Then
        self.assertEqual(result, 2.5)

    def test3(self):
        # Given
        nums1 = [1]
        nums2 = []

        # When
        result = self.solution(nums1, nums2)

        # Then
        self.assertEqual(result, 1.0)
