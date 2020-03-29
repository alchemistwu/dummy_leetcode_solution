"""
Link: https://leetcode.com/problems/unique-paths-ii/
Intro: A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
"""
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        value = 1    
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                value = 0
            obstacleGrid[i][0] = value
        value = 1    
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                value = 0
            obstacleGrid[0][j] = value
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]
        
        return obstacleGrid[-1][-1]
if __name__ == "__main__":
    s = Solution()
    input_matrix = [[0,0,0],[0,1,0],[0,0,0]]

    print(s.uniquePathsWithObstacles(input_matrix))
