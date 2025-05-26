from unittest import TestCase

from problems.average_of_levels_in_binary_tree import Solution, TreeNode
from tests import PSTestCase


class TestCases(TestCase, PSTestCase):
    def setUp(self):
        self.solution_object = Solution()
    
    def solution(self, *args, **kwargs) -> any:
        return self.solution_object.averageOfLevels(*args, **kwargs)

    def test_example_1(self):
        # Given
        root = TreeNode(
            val=3,
            left=TreeNode(9),
            right=TreeNode(
                val=20,
                left=TreeNode(15),
                right=TreeNode(7),
            ),
        )

        # When
        actual = self.solution(root)

        # Then
        expected = [3.00000, 14.50000, 11.00000]
        self.assertEqual(expected, actual)

    def test_example_2(self):
        # Given
        root = TreeNode(
            val=3,
            left=TreeNode(
                val=9,
                left=TreeNode(15),
                right=TreeNode(7)
            ),
            right=TreeNode(20)
        )

        # When
        actual = self.solution(root)

        # Then
        expected = [3.00000, 14.50000, 11.00000]
        self.assertEqual(expected, actual)
