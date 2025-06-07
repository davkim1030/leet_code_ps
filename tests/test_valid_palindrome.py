import pytest

from problems.valid_palindrome import Solution


@pytest.mark.parametrize(
    "s, expected", [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
    ]
)
def test(s, expected):
    actual = Solution().isPalindrome(s)

    assert actual == expected
