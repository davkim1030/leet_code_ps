# https://leetcode.com/problems/median-of-two-sorted-arrays/
# 4. Median of Two Sorted Arrays
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        full_length = m + n
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        start, end = 0, m
        while start <= end:
            part1 = (start + end) // 2
            part2 = (full_length + 1) // 2 - part1

            max_left1 = nums1[part1 - 1] if part1 != 0 else float("-inf")
            min_right1 = nums1[part1] if part1 != m else float("inf")

            max_left2 = nums2[part2 - 1] if part2 != 0 else float("-inf")
            min_right2 = nums2[part2] if part2 != n else float("inf")

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if full_length % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                end -= 1
            else:
                start += 1

        return 0.0

