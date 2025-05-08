from typing import *
from math import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        minElement = inf

        start,end = 0, len(nums)-1

        while start<=end:
            mid = start + (end-start)//2

            if nums[start]<=nums[mid]:
                minElement = min(minElement, nums[start])
                start = mid+1
            else:
                minElement = min(minElement, nums[mid])
                end = mid-1
        
        return minElement