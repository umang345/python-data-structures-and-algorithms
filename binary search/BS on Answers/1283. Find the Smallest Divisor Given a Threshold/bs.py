from functools import reduce
from math import ceil,inf
from typing import *

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''
        nums = [1,2,5,9], threshold = 6
               
        div  = 5
        [1,1,1,2]
        [1, max(arr)]      TC ->  O(n)  +  O(log(max(arr)) * O(n)) 
        '''

        if threshold < len(nums):
            return -1
    
        maxNum = reduce(lambda acc,x : max(acc,x), nums, nums[0])
        low, high = 1, maxNum
        result = inf
        while low<=high:
            divisor = low + (high-low)//2
            
            if self.computeDivisionSum(nums, divisor, threshold):
                result = min(result, divisor)
                high = divisor-1
            else:
                low = divisor+1
        
        return result


    def computeDivisionSum(self, nums:List[int], divisor:int, threshold:int) -> bool:
        sumOfDiv = 0
        for num in nums :
            sumOfDiv += ceil(num/divisor)
        
        return sumOfDiv <= threshold