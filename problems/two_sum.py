# https://leetcode.com/problems/two-sum/
# 1. Two Sum
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index_hash = {}
        for i, num in enumerate(nums):
            if target - num in num_to_index_hash:
                return [num_to_index_hash[target - num], i]
            num_to_index_hash[num] = i
