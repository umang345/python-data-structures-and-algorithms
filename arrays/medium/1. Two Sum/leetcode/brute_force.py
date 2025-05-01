from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for outerIndex in range(len(nums)):
            for innerIndex in range(outerIndex+1, len(nums)):
                if nums[outerIndex]+nums[innerIndex] == target:
                    return [outerIndex, innerIndex]

        raise Exception("Invalid Input")


'''
Time Complexity : [n-1 + n-2 + n-3 + ........+1]   n(n-1)/2  O(n^2)
Space Complexity : O(1)
'''