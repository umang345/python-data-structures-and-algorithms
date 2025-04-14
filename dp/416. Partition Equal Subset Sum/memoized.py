from typing import *
from functools import reduce

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        sumOfElements = reduce(lambda acc,x : acc+x, nums, 0)
        if sumOfElements%2!=0:
            return False

        cache = dict()
        return self.helper(0, sumOfElements//2, nums, cache)


    def helper(self, index:int, target:int, nums:list, cache:dict) -> bool:
        if target == 0:
            return True

        if index >= len(nums):
            return False
        
        key = f"{index}-{target}"
        if not cache.get(key) is None:
            return cache[key]
        
        if nums[index] > target:
            cache[key] = self.helper(index+1, target, nums, cache)
        else:
            cache[key] = self.helper(index+1, target - nums[index], nums, cache) or self.helper(index+1, target, nums, cache)
        return cache[key]