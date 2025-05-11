from math import *
from typing import *

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n,m = len(mat), len(mat[0])

        low, high = 0,m-1

        while low<=high:
            mid = low + (high-low)//2
            
            maxElementRowIndex = self.findMaxElementInColumn(mat, mid)
            left = mat[maxElementRowIndex][mid-1] if mid-1>=0 else -1
            right = mat[maxElementRowIndex][mid+1] if mid+1<m else -1

            if mat[maxElementRowIndex][mid] > left and mat[maxElementRowIndex][mid] > right:
                return [maxElementRowIndex,mid]

            if mat[maxElementRowIndex][mid]>left:
                low = mid+1
            else:
                high = mid-1
        
        return None


    def findMaxElementInColumn(self, mat:list[list[int]], colIndex) -> int:

        rowIndex = -1
        maxElement = -inf
        for index in range(len(mat)):
            if maxElement < mat[index][colIndex]:
                maxElement = mat[index][colIndex]
                rowIndex = index
        
        return rowIndex