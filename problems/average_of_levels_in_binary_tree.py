# https://leetcode.com/problems/average_of_levels_in_binary_tree/
# 637. Average of Levels in Binary Tree
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_averages = []
        queue = deque([root])

        while queue:
            node_cnt, level_sum = len(queue), 0
            for _ in range(node_cnt):
                current_node = queue.popleft()
                level_sum += current_node.val

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            level_averages.append(level_sum / node_cnt)
        return level_averages
