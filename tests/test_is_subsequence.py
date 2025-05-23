from unittest import TestCase

from problems.is_subsequence import Solution
from tests import PSTestCase


class TestCases(TestCase, PSTestCase):
    def setUp(self):
        self.solution_object = Solution()

    def solution(self, *args, **kwargs) -> any:
        return self.solution_object.isSubsequence(*args, **kwargs)

    def testcase1(self):
        # Given: abc, ahbgdc
        s = "abc"
        t = "ahbgdc"

        # When:
        result = self.solution(s=s, t=t)

        # Then: true
        self.assertEqual(True, result)

    def testcase2(self):
        # Given: axc
        s = "axc"
        t = "ahbgdc"

        # When:
        result = self.solution(s=s, t=t)

        # Then: false
        self.assertEqual(False, result)
