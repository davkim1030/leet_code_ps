from unittest import TestCase

from problems.longest_substring_without_repeating_characters import Solution
from tests import PSTestCase


class TestLongestSubstringWithoutRepeatingCharacters(TestCase, PSTestCase):
    def setUp(self):
        self.solution_object = Solution()

    def solution(self, *args, **kwargs) -> any:
        return self.solution_object.lengthOfLongestSubstring(*args, **kwargs)

    def test1(self):
        # Given
        s = "abcabcbb"

        # When
        result = self.solution(s)

        # Then
        self.assertEquals(result, 3)

    def test2(self):
        # Given
        s = "bbbbb"

        # When
        result = self.solution(s)

        # Then
        self.assertEquals(result, 1)

    def test3(self):
        # Given
        s = "pwwkew"

        # When
        result = self.solution(s)

        # Then
        self.assertEquals(result, 3)

    def test4(self):
        # Given
        s = "abba"

        # When
        result = self.solution(s)

        # Then
        self.assertEquals(result, 2)

