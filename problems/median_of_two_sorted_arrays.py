# https://leetcode.com/problems/median-of-two-sorted-arrays/
# 4. Median of Two Sorted Arrays
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        full_len = len(nums1) + len(nums2)
        finding_len = full_len // 2 + 1
        result = []

        i1, i2 = 0, 0
        while i1 + i2 < finding_len:
            if len(nums1) == i1:
                result.append(nums2[i2])
                i2 += 1
            elif len(nums2) == i2:
                result.append(nums1[i1])
                i1 += 1
            elif nums1[i1] <= nums2[i2]:
                result.append(nums1[i1])
                i1 += 1
            else:
                result.append(nums2[i2])
                i2 += 1

        if full_len % 2 == 0:
            return (result[-1] + result[-2]) / 2.0
        return result[-1]
