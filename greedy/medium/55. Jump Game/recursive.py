from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.helper(0,nums)

    def helper(self, index:int, nums:list) -> bool:
        if index>=len(nums)-1:
            return True
        
        for jump in range(1,nums[index]+1):
            if self.helper(index+jump, nums):
                return True
        
        return False