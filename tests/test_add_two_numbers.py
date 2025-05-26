import pytest

from problems.add_two_numbers import ListNode, Solution


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


@pytest.mark.parametrize(
    "l1, l2, expected", [
        (342, 465, 807),
        (0, 0, 0),
        (9_999_999, 9_999, 10_009_998),
        (0, 1, 1),
    ]
)
def testcase(l1, l2, expected):
    l1 = _int_to_node(l1)
    l2 = _int_to_node(l2)

    actual = Solution().addTwoNumbers(l1, l2)
    expected = _int_to_node(expected)

    assert _compare(expected, actual)
