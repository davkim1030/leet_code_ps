import pytest

from problems.is_subsequence import Solution


@pytest.mark.parametrize(
    "s, t, expected", [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
    ]
)
def test(s, t, expected):
    actual = Solution().isSubsequence(s, t)

    assert actual == expected
