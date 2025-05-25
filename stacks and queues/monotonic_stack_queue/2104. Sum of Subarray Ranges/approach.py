from collections import deque 
from typing import *

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        sumOfMin, sumOfMax = 0,0
        nse = self.findNextSmallerElement(nums)
        pse = self.findPrevSmallerElement(nums)
        nge = self.findNextGreaterElement(nums)
        pge = self.findPrevGreaterElement(nums)

        for index in range(len(nums)):
            sumOfMin+=(nums[index]*(nse[index]-index)*(index-pse[index]))
            sumOfMax+=(nums[index]*(nge[index]-index)*(index-pge[index]))
        
        return sumOfMax - sumOfMin


    def findPrevGreaterElement(self, nums:List[int]) -> List[int]:
        stack = deque()
        result = [-1]*len(nums)

        for index in range(len(nums)):
            while stack and nums[stack[0]] <= nums[index]:
                stack.popleft()
            
            if stack:
                result[index] = stack[0]
            
            stack.appendleft(index)
        
        return result

    def findNextGreaterElement(self, nums:List[int]) -> List[int]:
        stack = deque()
        result = [len(nums)]*len(nums)

        for index in range(len(nums)-1,-1,-1):
            while stack and nums[stack[0]] < nums[index]:
                stack.popleft()
            
            if stack:
                result[index] = stack[0]
            
            stack.appendleft(index)
        
        return result
    
    def findPrevSmallerElement(self, nums:List[int]) -> List[int]:
        stack = deque()
        result = [-1]*len(nums)

        for index in range(len(nums)):
            while stack and nums[stack[0]] >= nums[index]:
                stack.popleft()
            
            if stack:
                result[index] = stack[0]
            
            stack.appendleft(index)
        
        return result

    def findNextSmallerElement(self, nums:List[int]) -> List[int]:
        stack = deque()
        result = [len(nums)]*len(nums)

        for index in range(len(nums)-1,-1,-1):
            while stack and nums[stack[0]] > nums[index]:
                stack.popleft()
            
            if stack:
                result[index] = stack[0]
            
            stack.appendleft(index)
        
        return result