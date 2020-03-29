"""
[summary]
Link:https://leetcode.com/problems/unique-paths/
Intro:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

"""
import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dpMatrix = np.zeros((m, n), dtype=np.int)
        dpMatrix[:, 0] = 1
        dpMatrix[0, :] = 1
        for i in range(1, m):
            for j in range(1, n):
                dpMatrix[i][j] = dpMatrix[i][j - 1] + dpMatrix[i - 1][j]
        return dpMatrix[m - 1][n - 1]

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(7, 3))