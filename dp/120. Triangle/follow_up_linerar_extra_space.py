from typing import *
from functools import reduce

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if len(triangle)==0:
            return 0

        rows = len(triangle)
        dp = [0]*rows
        dp[0] = triangle[0][0]

        for rowIndex in range(1, rows):
            cols = len(triangle[rowIndex])
            currentState = [0]*cols
            for colIndex in range(cols):
                currentState[colIndex] = triangle[rowIndex][colIndex]
                if colIndex == 0:
                    currentState[colIndex]+=dp[colIndex]
                elif colIndex == cols-1:
                    currentState[colIndex]+=dp[colIndex-1]
                else:
                    currentState[colIndex]+=min(
                        dp[colIndex],dp[colIndex-1]
                    )

            for colIndex in range(cols):
                dp[colIndex] = currentState[colIndex]

        return reduce(lambda acc, x:min(acc,x), dp, dp[0])


