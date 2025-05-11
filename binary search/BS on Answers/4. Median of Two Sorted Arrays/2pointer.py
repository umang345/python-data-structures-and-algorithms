from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m = len(nums1), len(nums2)
        if (n+m)%2!=0:
            midIndex = (n+m)//2
            return self.helper(nums1, nums2, midIndex)
        else:
            mid1 = ((n+m)//2)-1
            mid2 = (n+m)//2
            elementAtMid1 = self.helper(nums1, nums2, mid1)
            elementAtMid2 = self.helper(nums1, nums2, mid2)
            return (elementAtMid1 + elementAtMid2)/2

    def helper(self, nums1:list, nums2:list, targetIndex:int)->int:
        p1,p2,index = 0,0,0
        currElement = -1

        while index<=targetIndex and p1<len(nums1) and p2 < len(nums2):
            if nums1[p1]<=nums2[p2]:
                currElement = nums1[p1]
                p1+=1
            else:
                currElement = nums2[p2]
                p2+=1
            index+=1
        
        while index<=targetIndex and p1<len(nums1):
            currElement = nums1[p1]
            p1+=1
            index+=1
        
        while index<=targetIndex and p2<len(nums2):
            currElement = nums2[p2]
            p2+=1
            index+=1
        
        return currElement
    
'''
TC  -> O((n+m))
SC  -> O(1)
'''