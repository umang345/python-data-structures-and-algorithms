from typing import *

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        return self.helper(0,0,matrix)

    def helper(self, row, col, matrix) -> int:
        if row >= len(matrix):
            return 0
        if col < 0 or col>=len(matrix[0]):
            return None
        
        if row == 0:
            minResult = None
            for colIndex in range(len(matrix[0])):
                currentMin = matrix[0][colIndex] + self.helper(row+1, colIndex, matrix)
                if colIndex-1>=0:
                    currentMin = min(currentMin, matrix[0][colIndex] + self.helper(row+1, colIndex-1, matrix))
                if colIndex+1<len(matrix[0]):
                    currentMin = min(currentMin, matrix[0][colIndex] +  self.helper(row+1, colIndex+1, matrix))
                
                if minResult is None:
                    minResult = currentMin
                else:
                    if currentMin < minResult:
                        minResult = currentMin
            
            return minResult
        else:
            currentMin = matrix[row][col] +  self.helper(row+1, col, matrix)
            if col-1>=0:
                currentMin = min(currentMin,matrix[row][col] +  self.helper(row+1, col-1, matrix))
            if col+1<len(matrix[0]):
                currentMin = min(currentMin,matrix[row][col] +  self.helper(row+1, col+1, matrix))
            return currentMin
                
                

