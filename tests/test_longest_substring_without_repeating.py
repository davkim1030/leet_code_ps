import pytest

from problems.longest_substring_without_repeating_characters import Solution


@pytest.mark.parametrize(
    "s, expected", [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("abba", 2),
    ]
)
def test(s, expected):
    actual = Solution().lengthOfLongestSubstring(s)

    assert actual == expected
