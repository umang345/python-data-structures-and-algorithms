from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.helper(0,nums, dict())

    def helper(self, index:int, nums:list, dp:dict) -> bool:
        if index>=len(nums)-1:
            return True
        
        if not dp.get(index) is None:
            return dp[index]
        
        for jump in range(1,nums[index]+1):
            if self.helper(index+jump, nums,dp):
                dp[index] = True
                return dp[index]
        
        dp[index] = False
        return dp[index]