from typing import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        for index in range(len(nums)-k+1):
            windowLimit = index+k
            currMax = nums[index]
            for winIndex in range(index, windowLimit):
                currMax = max(currMax, nums[winIndex])
            
            result.append(currMax)
        
        return result

        