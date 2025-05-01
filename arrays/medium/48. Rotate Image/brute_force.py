from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        
        1 2 3      7 4 1
        4 5 6      8 5 2
        7 8 9      9 6 3
        
        00 01 02    20 10 00
        10 11 12    21 11 01 
        20 21 22    22 12 02

        i,j   ->    n-1-j,i
        """
        n = len(matrix)
        temp = [[-1 for col in range(n)] for row in range(n)]
        
        for row in range(n):
            for col in range(n):
                temp[row][col] = matrix[n-1-col][row]

        for row in range(n):
            for col in range(n):
                matrix[row][col] = temp[row][col]