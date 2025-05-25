from typing import *

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        [1,6,3,9,2,3,90]
        ''' 
        result = [-1]*len(nums)
        for index in range(len(nums)):
            result[index] = self.nextGreaterForIndex(nums, index)
        
        return result
    
    def nextGreaterForIndex(self, nums:list, index) -> int:
        for nextIndex in range(index+1, len(nums)):
            if nums[nextIndex] > nums[index]:
                return nums[nextIndex]
        
        for nextIndex in range(index):
            if nums[nextIndex] > nums[index]:
                return nums[nextIndex]
        
        return -1