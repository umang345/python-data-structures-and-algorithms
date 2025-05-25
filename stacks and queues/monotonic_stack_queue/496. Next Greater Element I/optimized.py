from collections import deque
from typing import *


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = [-1]*len(nums1)
        nge = [-1]*len(nums2)
        stack = deque()

        for index in range(len(nums2)-1,-1,-1):
            while len(stack)>0 and stack[0] < nums2[index]:
                stack.popleft()
            
            if len(stack)>0:
                nge[index] = stack[0]
            
            stack.appendleft(nums2[index])

        for index1 in range(len(nums1)):
            for index2 in range(len(nums2)):
                if nums1[index1] == nums2[index2]:
                    result[index1] = nge[index2]
                    break
        
        return result