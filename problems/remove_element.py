# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
# 27. Remove Element
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        EMPTY = "_"

        element_count = len(nums)
        write_pos = element_count - 1
        read_pos = 0

        while read_pos < len(nums) and read_pos <= write_pos:
            if nums[write_pos] == EMPTY:
                break

            if nums[read_pos] == val:
                nums[read_pos] = nums[write_pos]
                nums[write_pos] = "_"
                element_count -= 1
                write_pos -= 1
            else:
                read_pos += 1
        return element_count
