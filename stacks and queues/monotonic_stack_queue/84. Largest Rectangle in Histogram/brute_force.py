from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        maxArea = 0
        for index in range(n):
            leftSmallerIndex, rightSmallerIndex = index, index

            while leftSmallerIndex>=0 and heights[leftSmallerIndex]>=heights[index]:
                leftSmallerIndex-=1
            
            while rightSmallerIndex<n and heights[rightSmallerIndex]>=heights[index]:
                rightSmallerIndex+=1
            
            width = rightSmallerIndex - leftSmallerIndex - 1
            maxArea = max(maxArea, heights[index]*width)
        
        return maxArea
            
