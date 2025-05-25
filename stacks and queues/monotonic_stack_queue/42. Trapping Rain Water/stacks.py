from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        leftGreater, rightGreater = [0]*n, [0]*n

        leftGreater[0], rightGreater[-1] = height[0], height[-1]

        for index in range(1, n):
            leftGreater[index] = max(height[index], leftGreater[index-1])

        for index in range(n-2, -1, -1):
            rightGreater[index] = max(height[index], rightGreater[index+1])

        result = 0
        for index in range(1, n-1):
            if min(leftGreater[index], rightGreater[index]) > height[index]:
                result+=(min(leftGreater[index], rightGreater[index]) - height[index])
        
        return result