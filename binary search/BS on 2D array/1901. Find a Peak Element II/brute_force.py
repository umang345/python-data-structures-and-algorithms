from typing import *

class Solution:
    def findPeakGrid(self, matrix: List[List[int]]) -> List[int]:
        n,m = len(matrix), len(matrix[0])

        for rowIndex in range(n):
            for colIndex in range(m):
                top = matrix[rowIndex-1][colIndex] if rowIndex-1>=0 else -1
                left = matrix[rowIndex][colIndex-1] if colIndex-1>=0 else -1
                right = matrix[rowIndex][colIndex+1] if colIndex+1<m else -1
                bottom = matrix[rowIndex+1][colIndex] if rowIndex+1<n else -1

                element = matrix[rowIndex][colIndex]
                if element>top and element>bottom and element>left and element>right:
                    return [rowIndex, colIndex]
        
        return -1