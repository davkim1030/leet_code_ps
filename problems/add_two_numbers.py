# https://leetcode.com/problems/add-two-numbers
# 2. Add Two Numbers
from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        next_node = result

        carry = 0
        has_next = True
        while has_next:
            tmp = (
                    (l1.val if l1 else 0) +
                    (l2.val if l2 else 0) +
                    carry
            )
            carry, result_value = divmod(tmp, 10)
            next_node.val = result_value

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            has_next = any((l1, l2, carry))
            if has_next:
                next_node.next = ListNode()
                next_node = next_node.next

        return result

