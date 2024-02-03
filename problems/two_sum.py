# https://leetcode.com/problems/two-sum/
# 1. Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        num_to_index_hash = {}
        for i, num in enumerate(nums):
            if target - num in num_to_index_hash:
                return [num_to_index_hash[target - num], i]
            num_to_index_hash[num] = i
