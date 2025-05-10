from functools import reduce
from math import ceil
from typing import *

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''
        nums = [1,2,5,9], threshold = 6
               
        div  = 5
        [1,1,1,2]
        [1, max(arr)]      TC ->  O(n)  +  O(max(arr) * O(n)) 
        '''

        if threshold < len(nums):
            return -1
    
        maxNum = reduce(lambda acc,x : max(acc,x), nums, nums[0])

        for divisor in range(1, maxNum+1):
            isDivSubPossible = self.computeDivisionSum(nums, divisor, threshold)
            if isDivSubPossible:
                return divisor
        
        return -1

    def computeDivisionSum(self, nums:List[int], divisor:int, threshold:int) -> bool:
        sumOfDiv = 0
        for num in nums :
            sumOfDiv += ceil(num/divisor)
        
        return sumOfDiv <= threshold
        
