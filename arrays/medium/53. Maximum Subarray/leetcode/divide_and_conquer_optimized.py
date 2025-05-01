from typing import *
from math import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixMaxSum = [nums[index] for index in range(len(nums))]
        suffixMaxSum = [nums[index] for index in range(len(nums))]

        for index in range(1, len(nums)):
            prefixMaxSum[index] += max(0, prefixMaxSum[index-1])
        
        for index in range(len(nums)-2, -1, -1):
            suffixMaxSum[index] += max(0, suffixMaxSum[index+1])
        
        return self.helper(nums,0, len(nums)-1,prefixMaxSum, suffixMaxSum)

    def helper(self, nums:list[int], start, end, prefixMaxSum:list, suffixMaxSum:int):
        if start == end:
            return nums[start]
        if start>end:
            return -inf

        mid = start + (end-start)//2
        return max(
            prefixMaxSum[mid]+suffixMaxSum[mid+1],
            max(
                self.helper(nums, start, mid,prefixMaxSum,suffixMaxSum),
                self.helper(nums, mid+1, end,prefixMaxSum,suffixMaxSum)
            )
        )
    
'''
Time Complexity -> T(n) = 2T(n/2)    -> O(N)
Space Complexity -> O(n) + O(n) + O(logn)
'''