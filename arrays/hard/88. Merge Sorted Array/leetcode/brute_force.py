from typing import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = [0]*(m+n)
        currIndex = 0

        i,j = 0,0
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                temp[currIndex] = nums1[i]
                i+=1
            else:
                temp[currIndex] = nums2[j]
                j+=1
            currIndex+=1
        
        while i<m:
            temp[currIndex] = nums1[i]
            currIndex+=1
            i+=1
        
        while j<n:
            temp[currIndex] = nums2[j]
            j+=1
            currIndex+=1
        
        for index in range(m+n):
            nums1[index] = temp[index]

'''
TC   O(m+n) + O(m+n)
SC   O(m+n)
'''
        
        
