from typing import *
from math import *

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        col0 = 0
        rowCount, colCount = len(matrix), len(matrix[0])

        for row in range(rowCount):
            for col in range(colCount):
                if matrix[row][col] == 0:
                    if col==0:
                        col0 = inf
                    else:
                        matrix[0][col] = inf

                    matrix[row][0] = inf

        for row in range(rowCount-1, -1, -1):
            for col in range(colCount-1, -1, -1):
                if col==0:
                    if col0 == inf:
                        matrix[row][col] = 0
                else:
                    if matrix[0][col] == inf:
                        matrix[row][col] = 0
                
                if matrix[row][0]==inf:
                    matrix[row][col] = 0