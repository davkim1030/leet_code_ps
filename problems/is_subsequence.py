# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pos = 0
        max_len = len(s)

        for c in t:
            if s_pos >= max_len:
                break

            if s[s_pos] == c:
                s_pos += 1

        return s_pos == max_len
