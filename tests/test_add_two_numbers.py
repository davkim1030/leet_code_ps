from unittest import TestCase

from problems.add_two_numbers import ListNode, Solution


class TestCases(TestCase):
    @staticmethod
    def _int_to_node(val: int) -> ListNode:
        if val == 0:
            return ListNode()

        result = ListNode()
        next_node = result
        while val > 0:
            val, mod = divmod(val, 10)
            next_node.val = mod
            if val > 0:
                next_node.next = ListNode()
                next_node = next_node.next
        return result

    @staticmethod
    def _compare(l1: ListNode, l2: ListNode) -> bool:
        has_next = True
        while has_next:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
            has_next = any((l1, l2))
        if bool(l1) != bool(l2):
            return False
        return True

    def testcase1(self):
        # Given: 342 + 465
        l1 = self._int_to_node(342)
        l2 = self._int_to_node(465)

        # When
        result = Solution().addTwoNumbers(l1, l2)

        # Then: 807
        self.assertTrue(self._compare(result, self._int_to_node(807)))

    def testcase2(self):
        # Given: 0 + 0
        l1 = ListNode(0)
        l2 = ListNode(0)

        # When
        result = Solution().addTwoNumbers(l1, l2)

        # Then: 0
        self.assertTrue(self._compare(result, ListNode(0)))

    def testcase3(self):
        # Given: 9,999,999 + 9,999
        l1 = self._int_to_node(9_999_999)
        l2 = self._int_to_node(9_999)

        # When
        result = Solution().addTwoNumbers(l1, l2)

        # Then: 10,009,998
        self.assertTrue(self._compare(result, self._int_to_node(10_009_998)))

    def testcase4(self):
        # Given: 0 + 1
        l1 = ListNode()
        l2 = ListNode(1)

        # When
        result = Solution().addTwoNumbers(l1, l2)

        # Then: 1
        self.assertTrue(self._compare(result, ListNode(1)))
