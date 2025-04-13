from functools import reduce
from typing import *

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        rows = len(triangle)
        cols = len(triangle[-1])
        dp = [[0 for colIndex in range(cols)] for rowIndex in range(rows)]
        dp[0][0] = triangle[0][0]
        for rowIndex in range(1, rows):
            for colIndex in range(0, len(triangle[rowIndex])):
                dp[rowIndex][colIndex] = triangle[rowIndex][colIndex]
                if colIndex==0:
                    dp[rowIndex][colIndex]+=dp[rowIndex-1][colIndex]
                elif colIndex == len(triangle[rowIndex])-1:
                    dp[rowIndex][colIndex]+=dp[rowIndex-1][colIndex-1]
                else:
                    dp[rowIndex][colIndex]+=min(
                        dp[rowIndex-1][colIndex],
                        dp[rowIndex-1][colIndex-1]
                    )
                

        return reduce(lambda acc, x: min(acc,x), dp[-1], dp[-1][0])