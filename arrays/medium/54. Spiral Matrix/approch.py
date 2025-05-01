from typing import *

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])

        left, right = 0, n-1
        up, down = 0, m-1
        result = []

        while(left<=right and up <= down):
            for index in range(left, right+1):
                result.append(matrix[up][index])
            
            up+=1
            if up>down:
                break

            for index in range(up, down+1):
                result.append(matrix[index][right])
            
            right-=1
            if left>right:
                break

            for index in range(right, left-1, -1):
                result.append(matrix[down][index])

            down-=1
            if up>down:
                break

            for index in range(down, up-1,-1):
                result.append(matrix[index][left])

            left+=1

        return result