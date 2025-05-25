from collections import *
from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nse = self.findNextSmallerElements(heights)
        pse = self.findPrevSmallerElements(heights)

        

        maxArea = 0
        for index in range(len(heights)):
            width = nse[index] - pse[index] - 1
            maxArea = max(maxArea, width*heights[index])
        
        return maxArea

    def findPrevSmallerElements(self, nums:List[int]) -> List[int]:
        stack = deque()

        result = [-1]*len(nums)

        for index in range(len(nums)):
            while stack and nums[stack[0]]>=nums[index]:
                stack.popleft()
            
            if stack:
                result[index] = stack[0]
            
            stack.appendleft(index)
        
        return result
    
    def findNextSmallerElements(self, nums:List[int]) -> List[int]:
        stack = deque()

        result = [len(nums)]*len(nums)

        for index in range(len(nums)-1, -1, -1):
            while stack and nums[stack[0]]>=nums[index]:
                stack.popleft()
            
            if stack:
                result[index] = stack[0]
            
            stack.appendleft(index)
        
        return result