from typing import *

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0

        for startIndex in range(len(nums)):
            currSum = 0
            for index in range(startIndex, len(nums)):
                currSum+=nums[index]
                if currSum > goal:
                    break
                if currSum == goal:
                    count+=1
        
        return count