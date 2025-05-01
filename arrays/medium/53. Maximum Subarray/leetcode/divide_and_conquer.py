from typing import *
from math import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums,0, len(nums)-1)

    def helper(self, nums:list[int], start, end):
        if start>end:
            return -inf

        mid = start + (end-start)//2
        leftMaxSum, rightMaxSum = 0,0
        currLeftSum, currRightSum = 0,0

        for index in range(mid-1, start-1, -1):
            currLeftSum+=nums[index]
            if leftMaxSum < currLeftSum:
                leftMaxSum = currLeftSum
            
        for index in range(mid+1, end+1):
            currRightSum+=nums[index]
            if rightMaxSum < currRightSum:
                rightMaxSum = currRightSum

        return max(
            leftMaxSum+nums[mid]+rightMaxSum,
            max(
                self.helper(nums, start, mid-1),
                self.helper(nums, mid+1, end)
            )
        )


'''
Time Complexity : T(n) = 2T(n/2) + n     O(nlogn)
Space Complexity : O(logn) recursive stack
'''