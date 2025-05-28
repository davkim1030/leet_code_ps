# https://leetcode.com/problems/house_robber/
# 198. House Robber
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        stashed = [0] * len(nums)
        stashed[:2] = nums[:2]

        for i in range(2, len(nums)):
            stashed[i] = max(stashed[i - 2], stashed[i - 3] if i > 2 else 0) + nums[i]
        return max(stashed[-2:])
