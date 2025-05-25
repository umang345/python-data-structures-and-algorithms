from collections import deque
from typing import *

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        row = [0]*len(matrix[0])
        maxCount = 0
        for index in range(len(matrix)):
            for colIndex in range(len(matrix[0])):
                if matrix[index][colIndex]=="0":
                    row[colIndex] = 0
                else:
                    row[colIndex]+=1
            maxCount = max(maxCount, self.helper(row))
        
        return maxCount


    def helper(self, row:List[int]) -> int:
        nse = self.getNextSmallerElements(row)
        pse = self.getPrevSmallerElements(row)
        
        maxCount = 0
        for index in range(len(row)):
            width = nse[index] - pse[index] - 1
            maxCount = max(maxCount, width * row[index])
        
        return maxCount

    def getPrevSmallerElements(self, row:List[int]) -> List[int]:
        stack = deque()
        result = [-1]*len(row)

        for index in range(len(row)):
            while stack and row[stack[0]]>=row[index]:
                stack.popleft()
            
            if stack:
                result[index] = stack[0] 
            
            stack.appendleft(index)
        
        return result    

    def getNextSmallerElements(self, row:List[int]) -> List[int]:
        stack = deque()
        result = [len(row)]*len(row)

        for index in range(len(row)-1, -1, -1):
            while stack and row[stack[0]]>=row[index]:
                stack.popleft()
            
            if stack:
                result[index] = stack[0] 
            
            stack.appendleft(index)
        
        return result