from typing import *
from functools import reduce

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1 for num in range(len(nums))]

        for index in range(len(nums)):
            for compare in range(index):
                if nums[index] > nums[compare]:
                    if dp[index] <= dp[compare]:
                        dp[index] = 1 + dp[compare]

        result = reduce(lambda acc, x: max(acc,x),  dp, dp[0])
        return result
