from typing import *

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[None for colIndex in range(len(matrix[0]))] for rowIndex in range(len(matrix))]
        return self.helper(0,0,matrix,dp)

    def helper(self, row, col, matrix, dp) -> int:
        if row >= len(matrix):
            return 0
        if col < 0 or col>=len(matrix[0]):
            return None

        if not dp[row][col] is None:
            return dp[row][col]
        
        if row == 0:
            minResult = None
            for colIndex in range(len(matrix[0])):
                currentMin = matrix[0][colIndex] + self.helper(row+1, colIndex, matrix,dp)
                if colIndex-1>=0:
                    currentMin = min(currentMin, matrix[0][colIndex] + self.helper(row+1, colIndex-1, matrix,dp))
                if colIndex+1<len(matrix[0]):
                    currentMin = min(currentMin, matrix[0][colIndex] +  self.helper(row+1, colIndex+1, matrix,dp))
                
                if minResult is None:
                    minResult = currentMin
                else:
                    if currentMin < minResult:
                        minResult = currentMin

            dp[row][col] = minResult
            return minResult
        else:
            currentMin = matrix[row][col] +  self.helper(row+1, col, matrix,dp)
            if col-1>=0:
                currentMin = min(currentMin,matrix[row][col] +  self.helper(row+1, col-1, matrix,dp))
            if col+1<len(matrix[0]):
                currentMin = min(currentMin,matrix[row][col] +  self.helper(row+1, col+1, matrix,dp))

            dp[row][col] = currentMin
            return currentMin