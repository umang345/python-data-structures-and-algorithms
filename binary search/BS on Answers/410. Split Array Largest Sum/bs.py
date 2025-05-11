from functools import reduce
from typing import *
from math import inf

from functools import reduce

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        maxElement = reduce(lambda acc,x : max(acc,x), nums,nums[0])
        totalSum = reduce(lambda acc,x : acc+x, nums, 0)

        result = inf
        low, high = maxElement, totalSum
        while low<=high:
            largestSumAllowed = low + (high-low)//2
            if self.helper(nums, k, largestSumAllowed):
                result = min(result, largestSumAllowed)
                high = largestSumAllowed-1
            else:
                low = largestSumAllowed+1
        
        return result

    
    def helper(self,nums:list[int], k:int, sumAllowed:int) -> bool:

        arrCount = 1
        currSum = 0

        for num in nums:
            currSum+=num
            if currSum > sumAllowed:
                arrCount+=1
                currSum = num
        
        return arrCount <= k