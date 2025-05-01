from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = None
        for startIndex in range(len(nums)):
            currSum = 0
            for currIndex in range(startIndex, len(nums)):
                currSum+=nums[currIndex]
                if maxSum is None or maxSum < currSum:
                    maxSum = currSum
        
        return maxSum


'''
TC -> O(n^2)
SC -> O(1)
'''