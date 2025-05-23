from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        minLimit, maxLimit = 0,0

        while maxLimit < len(nums)-1:
            updatedMax = minLimit

            for index in range(minLimit, maxLimit+1):
                updatedMax = max(updatedMax,index+nums[index])
            
            if updatedMax <= maxLimit:
                return False
            
            minLimit = maxLimit+1
            maxLimit = updatedMax
        
        return True