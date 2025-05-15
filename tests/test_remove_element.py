from unittest import TestCase

from problems.remove_element import Solution
from tests import PSTestCase


class TestCases(TestCase, PSTestCase):
    def setUp(self):
        self.solution_object = Solution()

    def solution(self, *args, **kwargs) -> any:
        return self.solution_object.removeElement(*args, **kwargs)

    def testcase1(self):
        # Given
        nums = [2, 3, 3, 2]
        val = 3

        # When
        result = self.solution(nums=nums, val=val)

        # Then
        self.assertEqual([2, 2], nums[:result])

    def testcase2(self):
        # Given
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2

        # When
        result = self.solution(nums=nums, val=val)

        # Then
        self.assertEqual([0, 1, 4, 0, 3], nums[:result])
