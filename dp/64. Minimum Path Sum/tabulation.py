from typing import *

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        rows, cols = len(grid), len(grid[0])
        dp = [[-1 for colIndex in range(cols)] for rowIndex in range(rows)]
        
        for rowIndex in range(rows):
            for colIndex in range(cols):
                if rowIndex == 0 and colIndex == 0:
                    dp[rowIndex][colIndex] = grid[rowIndex][colIndex]
                elif rowIndex == 0 and colIndex !=0:
                    dp[rowIndex][colIndex] = grid[rowIndex][colIndex]+ dp[rowIndex][colIndex-1]
                elif rowIndex != 0 and colIndex ==0:
                    dp[rowIndex][colIndex] = grid[rowIndex][colIndex]+ dp[rowIndex-1][colIndex]
                else:
                    dp[rowIndex][colIndex] = grid[rowIndex][colIndex]+ \
                    min(dp[rowIndex-1][colIndex], dp[rowIndex][colIndex-1])

        return dp[rows-1][cols-1]