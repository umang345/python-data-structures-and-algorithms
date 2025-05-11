from typing import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowIndex = -1

        low, high = 0, len(matrix)-1

        while low<=high:
            mid = low + (high-low)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0] > target:
                high = mid-1
            else:
                rowIndex = mid
                low = mid+1
        
        if rowIndex == -1:
            return False

        low, high = 0, len(matrix[rowIndex])-1
        while low<=high:
            mid = low + (high-low)//2
            if matrix[rowIndex][mid] == target:
                return True
            elif matrix[rowIndex][mid] > target:
                high = mid-1
            else:
                low = mid+1
        
        return False
        
        