from typing import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        minLimit, maxLimit = 0,0
        count=0

        while maxLimit<len(nums)-1:
            count+=1
            updatedMax = minLimit
            for index in range(minLimit, maxLimit+1):
                updatedMax = max(updatedMax, index+nums[index])
            
            minLimit = maxLimit+1
            maxLimit = updatedMax
        
        return count