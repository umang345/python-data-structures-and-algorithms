
from typing import *

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
         e  o  e  o  e  o  e  o  e
        [1, 1, 2, 3, 3, 4, 4, 8, 8]
         0  1  2  3  4  5  6  7  8

         e  o  e  o  e  o  e  o  e
        [1, 1, 2, 2, 3, 4, 4, 8, 8]

        (even, odd)
         3,3            first and even    -> go right
                        second and odd    -> go right  

        (odd, even)
         3,3            first and odd     -> go left
                        second and even   -> go left  
        '''

        if len(nums)==1:
            return nums[0]

        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]

        start,end = 1, len(nums)-2

        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]

            if (mid%2==0 and nums[mid]==nums[mid+1]) or (mid%2==1 and nums[mid]==nums[mid-1]):
                start = mid+1
            else:
                end = mid-1
        
        return -1

















