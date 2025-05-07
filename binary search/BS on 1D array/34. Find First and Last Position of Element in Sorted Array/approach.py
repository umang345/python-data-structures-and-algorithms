from typing import *

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self.firstPos(nums, target),
            self.lastPos(nums,target)
        ]
    
    def firstPos(self, nums:List[int], target:int) -> int:

        result = -1
        start,end = 0, len(nums)-1

        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]==target:
                result = mid

            if nums[mid]>=target:
                end = mid-1
            else:
                start = mid+1
        
        return result
    
    def lastPos(self, nums:List[int], target:int) -> int:
        result = -1
        start, end = 0, len(nums)-1

        while start<=end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                result = mid

            if nums[mid] <= target:
                start = mid+1
            else:
                end = mid-1
            
        return result