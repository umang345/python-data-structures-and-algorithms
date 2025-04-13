from functools import *
from typing import *

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [0]*cols

        for rowIndex in range(rows-1, -1, -1):
            currentState = [0]*cols
            for colIndex in range(cols-1, -1, -1):
                
                if rowIndex == rows-1:
                    currentState[colIndex] = matrix[rowIndex][colIndex]
                else:
                    
                    currentMin = dp[colIndex]
                    if colIndex-1>=0:
                        currentMin = min(currentMin, dp[colIndex-1])
                    if colIndex+1<cols:
                        currentMin = min(currentMin, dp[colIndex+1])
                    currentState[colIndex] = currentMin + matrix[rowIndex][colIndex]
            
            for colIndex in range(cols-1, -1, -1):
                dp[colIndex] = currentState[colIndex]

        return reduce(lambda acc,x:min(acc,x), dp, dp[0])