from collections import deque
from typing import *

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        result = [-1]*len(nums)
        stack = deque()
        for index in range(len(nums)-1,-1,-1):
            while len(stack)>0 and stack[0]<=nums[index]:
                stack.popleft()
            stack.appendleft(nums[index])
        
        for index in range(len(nums)-1,-1,-1):
            while len(stack)>0 and stack[0]<=nums[index]:
                stack.popleft()
            
            if len(stack)>0:
                result[index] = stack[0]
            
            stack.appendleft(nums[index])
        
        return result