from typing import *
from functools import reduce 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumOfElements = reduce(lambda acc,x : acc+x, nums, 0)
        if sumOfElements%2!=0:
            return False
        
        cache = [[False for target in range((sumOfElements//2)+1)] for index in range(len(nums)+1)]

        for index in range(len(nums)+1):
            cache[index][0] = True

        for index in range(1, len(nums)+1):
            for target in range(1, (sumOfElements//2)+1):
                if nums[index-1] > target:
                    cache[index][target] = cache[index-1][target]
                else:
                    cache[index][target] = cache[index-1][target - nums[index-1]] or cache[index-1][target]

        return cache[len(nums)][sumOfElements//2]