from typing import *

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sumOfMins = 0
        mod = (10**9)+7

        for index in range(len(arr)):
            currMin = arr[index]
            for nextIndex in range(index, len(arr)):
                currMin = min(currMin, arr[nextIndex])
                sumOfMins = (sumOfMins+currMin)%mod
        
        return sumOfMins