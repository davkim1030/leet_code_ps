# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3. Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        start, end = 0, 0
        hash_map = {}
        while end < len(s):
            current_char = s[end]
            if current_char not in s[start:end]:
                hash_map[current_char] = end
            else:
                start = hash_map[current_char] + 1
                hash_map[current_char] = end
            end += 1
            max_len = max(max_len, end - start)
        return max_len
