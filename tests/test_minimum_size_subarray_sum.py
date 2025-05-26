from unittest import TestCase

from problems.minimum_size_subarray_sum import Solution
from tests import PSTestCase


class TestCases(TestCase, PSTestCase):
    def setUp(self):
        self.solution_object = Solution()
    
    def solution(self, *args, **kwargs) -> any:
        return self.solution_object.minSubArrayLen(*args, **kwargs)

    def test_example_1(self):
        # Given: Example 1
        target = 7
        nums = [2, 3, 1, 2, 4, 3]

        # When
        result = self.solution(target=target, nums=nums)

        # Then
        self.assertEqual(2, result)

    def test_example_2(self):
        # Given: Example 2
        target = 4
        nums = [1, 4, 4]

        # When
        result = self.solution(target=target, nums=nums)

        # Then
        self.assertEqual(1, result)

    def test_example_3(self):
        # Given: Example 3
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]

        # When
        result = self.solution(target=target, nums=nums)

        # Then
        self.assertEqual(0, result)
