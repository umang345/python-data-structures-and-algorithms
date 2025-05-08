from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start,end = 0, len(nums)-1
        while start<=end:
            mid = start + (end-start)//2

            if nums[mid]==target:
                return True
            
            if nums[start]==nums[mid] and nums[mid]==nums[end]:
                start+=1
                end-=1
                continue
            
            if nums[start]<=nums[mid]:
                if target>=nums[start] and target<=nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if target>=nums[mid] and target<=nums[end]:
                    start = mid+1
                else:
                    end = mid-1
        
        return False
