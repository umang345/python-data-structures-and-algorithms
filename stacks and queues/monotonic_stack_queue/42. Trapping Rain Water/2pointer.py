from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax, rightMax = 0,0
        leftP, rightP = 0, len(height)-1

        result = 0

        while leftP < rightP:
            leftMax = max(leftMax,height[leftP])
            rightMax = max(rightMax, height[rightP])

            minHeight = min(height[leftP], height[rightP])

            if min(leftMax, rightMax) > minHeight:
                result+=(min(leftMax, rightMax) - minHeight)
            
            if leftMax<=rightMax:
                leftP+=1
            else:
                rightP-=1
        
        return result