from typing import *
from math import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.helper(nums, 0, 0)
    
    def helper(self, nums:list, index:int, jumps:int) -> int:
        if index >=len(nums)-1:
            return jumps
        
        currCount = inf

        for jump in range(1, nums[index]+1):
            result = self.helper(nums, index+jump, jumps+1)
            currCount = min(currCount, result)
        
        return currCount