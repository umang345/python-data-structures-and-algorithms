from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n,m = len(nums1), len(nums2)
        merged = [0]*(n+m)

        index,p1,p2 = 0,0,0
        while p1<n and p2<m:
            if nums1[p1]<=nums2[p2]:
                merged[index] = nums1[p1]
                p1+=1
            else:
                merged[index] = nums2[p2]
                p2+=1
            index+=1
        
        while p1<n:
            merged[index] = nums1[p1]
            index+=1
            p1+=1
        
        while p2<m:
            merged[index] = nums2[p2]
            index+=1
            p2+=1
        
        if (n+m)%2!=0:
            midIndex = (n+m)//2
            return merged[midIndex]
        else:
            mid1, mid2 = ((n+m)//2)-1, (n+m)//2
            return (merged[mid1]+merged[mid2])/2
        
'''
TC  -> O(n+m)
SC  -> O(n+m)
'''