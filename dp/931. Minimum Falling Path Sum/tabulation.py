from typing import *
from functools import *

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [ [0]*cols for rowIndex in range(rows) ]

        for rowIndex in range(rows-1, -1, -1):
            for colIndex in range(cols-1, -1, -1):

                if rowIndex == rows-1:
                    dp[rowIndex][colIndex] = matrix[rowIndex][colIndex]
                else:
                    currentMin = dp[rowIndex+1][colIndex]
                    if colIndex-1>=0:
                        currentMin = min(currentMin, dp[rowIndex+1][colIndex-1])
                    if colIndex+1<cols:
                        currentMin = min(currentMin, dp[rowIndex+1][colIndex+1])
                    dp[rowIndex][colIndex] = currentMin + matrix[rowIndex][colIndex]

        return reduce(lambda acc,x:min(acc,x), dp[0], dp[0][0])