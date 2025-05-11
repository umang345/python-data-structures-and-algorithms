from functools import reduce
from typing import *

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        maxElement = reduce(lambda acc,x : max(acc,x), nums,nums[0])
        totalSum = reduce(lambda acc,x : acc+x, nums, 0)

        for largestSumAllowed in range(maxElement, totalSum):
            if self.helper(nums, k, largestSumAllowed):
                return largestSumAllowed
        
        return -1

    def helper(self,nums:list[int], k:int, sumAllowed:int) -> bool:

        arrCount = 1
        currSum = 0

        for num in nums:
            currSum+=num
            if currSum > sumAllowed:
                arrCount+=1
                currSum = num
        
        return arrCount == k
    
'''
TC   k = sum-max+1           O(n)+O(n)+O(k*n)

'''