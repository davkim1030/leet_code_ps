from collections import deque
from typing import List

import pytest

from problems.average_of_levels_in_binary_tree import Solution, TreeNode


def _list_to_binary_tree(tree: List[int]) -> TreeNode:
    if not tree:
        return TreeNode()

    root = TreeNode(tree[0])
    queue = deque([root])
    idx = 1

    while queue and idx < len(tree):
        node = queue.popleft()
        # 왼쪽 자식
        if idx < len(tree) and tree[idx] is not None:
            node.left = TreeNode(tree[idx])
            queue.append(node.left)
        idx += 1
        # 오른쪽 자식
        if idx < len(tree) and tree[idx] is not None:
            node.right = TreeNode(tree[idx])
            queue.append(node.right)
        idx += 1

    return root


@pytest.mark.parametrize(
    "tree, expected", [
        ([3, 9, 20, None, None, 15, 7], [3.00000, 14.50000, 11.00000]),
        ([3, 9, 20, 15, 7], [3.00000, 14.50000, 11.00000])
    ]
)
def test(tree, expected):
    tree = _list_to_binary_tree(tree)

    actual = Solution().averageOfLevels(tree)

    assert actual == expected
