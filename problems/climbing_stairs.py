# https://leetcode.com/problems/climbing_stairs/
# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        jump_amounts = (1, 2)
        stairs = [0 for _ in range(n)]
        stairs[0], stairs[1] = 1, 2

        for i in range(n):
            for j in jump_amounts:
                if i - j >= 0 and i >= len(jump_amounts):
                    stairs[i] += stairs[i - j]
        print(stairs)
        return stairs[-1]
