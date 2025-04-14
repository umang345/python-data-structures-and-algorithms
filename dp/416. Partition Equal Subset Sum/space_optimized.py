from typing import *
from functools import reduce

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumOfElements = reduce(lambda acc,x : acc+x, nums, 0)
        if sumOfElements%2!=0:
            return False
        
        cache = [False for target in range((sumOfElements//2)+1)]
        cache[0] = True
        target = (sumOfElements//2)

        for index in range(len(nums)):
            context = [False for t in range(target+1)]
            context[0] = True
            for tar in range(1,target+1):
                if nums[index] > tar:
                    context[tar] = cache[tar]
                else:
                    context[tar] = cache[tar] or cache[tar - nums[index]]

            for index, element in enumerate(context):
                cache[index] = element
        
        return cache[target]