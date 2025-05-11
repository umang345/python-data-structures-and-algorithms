from typing import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n,m = len(matrix), len(matrix[0])

        row, col = 0, len(matrix[0])-1
        while row<n and col>=0:
            if matrix[row][col] == target:
                return True
            if target < matrix[row][col]:
                col-=1
            else:
                row+=1
        
        return False
