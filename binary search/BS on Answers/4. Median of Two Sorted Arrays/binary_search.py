from typing import *
from math import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        [2]   [1,3]

        mid = 0
        left1 = -inf
        right1 = 2
        left2 = 1
        right2 = 3  
        '''

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n,m = len(nums1), len(nums2)

        low,high = 0, n    # [3,5,67,90]
        while low <= high:
            mid = low + (high-low)//2
            elementsAtLeft = 0
            if (n+m)%2==0:
                elementsAtLeft = (n+m)//2
            else:
                elementsAtLeft = (n+m+1)//2
            
            left1 = nums1[mid-1] if mid-1>=0 else -inf
            right1 = nums1[mid] if mid<n else inf
            left2 = nums2[(elementsAtLeft - mid-1)] if (elementsAtLeft - mid-1)>=0 else -inf 
            right2 = nums2[(elementsAtLeft - mid)] if (elementsAtLeft - mid)<m else inf

            if (n+m)%2==0:
                if left1<=right2 and left2<=right1:
                    return (max(left1, left2) + min(right1, right2))/2
                if left1<=right2:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if left1<=right2 and left2<=right1:
                    return max(left1, left2)
                if left1<=right2:
                    low = mid+1
                else:
                    high = mid-1
