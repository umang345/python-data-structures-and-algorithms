from typing import *

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        sumOfMins, sumOfMax = 0,0

        for index in range(len(nums)):
            currMin, currMax = nums[index], nums[index]
            for nextIndex in range(index, len(nums)):
                currMin = min(currMin, nums[nextIndex])
                currMax = max(currMax, nums[nextIndex])
                sumOfMins+=currMin
                sumOfMax+=currMax
        
        return sumOfMax - sumOfMins