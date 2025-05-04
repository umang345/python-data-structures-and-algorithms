from typing import *

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        count = 0
        for index in range(len(nums)):
            for currIndex in range(index+1,len(nums)):
                if nums[index] > 2*nums[currIndex]:
                    count+=1
        return count