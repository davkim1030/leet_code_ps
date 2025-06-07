import pytest

from problems.word_break import Solution


@pytest.mark.parametrize(
    "s, wordDict, expected", [
        # ("leetcode", ["leet","code"], True),
        # ("applepenapple", ["apple","pen"], True),
        # ("catsandog", ["cats","dog","sand","and","cat"], False),
        # ("aaaaaaa", ["aaaa", "aaa"], True),
        # ("goalspecial", ["go","goal","goals","special"], True),
        # ("catscatdog", ["cat","cats","dog"], True),
        # ("aebbbbs", ["a","aeb","ebbbb","s","eb"], True),
        ("leeleet", ["lee", "leet"], True),
        # ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"], False),
    ]
)
def test(s, wordDict, expected):
    actual = Solution().wordBreak(s, wordDict)

    assert actual == expected
