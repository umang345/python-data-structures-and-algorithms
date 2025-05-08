from typing import *

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1

        for index in range(1, len(nums)-1):
            if nums[index] > nums[index-1] and nums[index]>nums[index+1]:
                return index
        
        return -1
