from unittest import TestCase

from problems.two_sum import Solution
from tests import PSTestCase


class TestCases(TestCase, PSTestCase):
    def setUp(self):
        self.solution_object = Solution()

    def solution(self, *args, **kwargs) -> any:
        return self.solution_object.twoSum(*args, **kwargs)

    def test_ascending_case_works(self):
        # Given: ascending list
        nums = [2, 7, 11, 15]
        target = 9

        # When
        result = self.solution(nums, target)

        # Then
        self.assertEqual(sorted(result), [0, 1])

    def test_descending_case_works(self):
        # Given: descending list
        nums = [15, 11, 7, 2]
        target = 9

        # When
        result = self.solution(nums, target)

        # Then
        self.assertEqual(sorted(result), [2, 3])

    def test_unsorted_case_works(self):
        # Given: unsorted list
        nums = [3, 2, 4]
        target = 6

        # When
        result = self.solution(nums, target)

        # Then
        self.assertEqual(sorted(result), [1, 2])

    def test_same_number_case_works(self):
        # Given: same number
        nums = [3, 3]
        target = 6

        # When
        result = Solution().twoSum(nums, target)

        # Then
        self.assertEqual(sorted(result), [0, 1])