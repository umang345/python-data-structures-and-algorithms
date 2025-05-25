from typing import *

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = [-1]*len(nums1)

        for index1 in range(len(nums1)):
            for index2 in range(len(nums2)):
                if nums1[index1] == nums2[index2]:
                    for nextIndex in range(index2+1, len(nums2)):
                        if nums2[nextIndex] > nums2[index2]:
                            result[index1] = nums2[nextIndex]
                            break
                    break
        
        return result