from collections import *
from typing import *

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        nse = self.getNextSmallerElements(arr)
        pse = self.getPreviousSmallerElements(arr)
        mod  = (10**9)+7

        sumOfMins = 0
        for index in range(len(arr)):
            sumOfMins = (sumOfMins + ((index - pse[index]) * (nse[index] - index) * arr[index]) )%mod

        return sumOfMins

    def getPreviousSmallerElements(self, arr:List[int]) -> List[int]:
        stack = deque()

        n = len(arr)
        result = [-1]*n

        for index in range(n):
            while stack and arr[stack[0]] >= arr[index]:
                stack.popleft()
            
            if stack:
                result[index] = stack[0]
            
            stack.appendleft(index)
        
        return result


    def getNextSmallerElements(self, arr:List[int]) -> List[int]:
        stack = deque()

        n = len(arr)
        result = [n]*n

        for index in range(n-1, -1, -1):
            while stack and arr[stack[0]] > arr[index]:
                stack.popleft()
            
            if stack:
                result[index] = stack[0]
            
            stack.appendleft(index)
        
        return result