from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        for diagnol in range(n):
            for index in range(diagnol,n):
                matrix[diagnol][index], matrix[index][diagnol] = matrix[index][diagnol], matrix[diagnol][index]

        for row in range(n):
            start, end = 0, n-1
            while start<end:
                matrix[row][start], matrix[row][end] = matrix[row][end], matrix[row][start]
                start+=1
                end-=1
        


        
        