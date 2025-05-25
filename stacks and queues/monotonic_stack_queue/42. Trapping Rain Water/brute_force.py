from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        for index in range(1,len(height)-1):
            leftIndex = index-1
            rightIndex = index+1
            leftMax, rightMax = height[index], height[index]
            while leftIndex>=0:
                leftMax = max(leftMax, height[leftIndex])
                leftIndex-=1
            while rightIndex<len(height):
                rightMax = max(rightMax, height[rightIndex])
                rightIndex+=1
            
            currWaterBlocks = min(leftMax, rightMax) - height[index]
            if currWaterBlocks>0:
                result+=currWaterBlocks
        
        return result