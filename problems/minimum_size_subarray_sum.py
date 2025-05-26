# https://leetcode.com/problems/minimum_size_subarray_sum/
# 209. Minimum Size Subarray Sum
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):
            current_sum += nums[right]
            # 합이 target 이상일 때 윈도우 크기 조정
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float("inf") else 0
