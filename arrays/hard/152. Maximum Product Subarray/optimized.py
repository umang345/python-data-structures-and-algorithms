from typing import *
from math import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        '''
        1) if all +ve  -> consider all
        2) if -ve numbers present -> take even -ve numbers
        3) 0s present

        [1,-3,4,0,6,-2,-4,8]
        [1,3,5,0,7,2,3]
        [-1] 0 [-3] 
        '''

        prefix, suffix = 1,1
        maxProd = -inf

        n = len(nums)
        for index in range(n):
            prefix*=(nums[index])
            suffix*=(nums[n-index-1])

            if prefix>maxProd:
                maxProd = prefix
            if suffix>maxProd:
                maxProd = suffix
            
            if nums[index]==0:
                prefix = 1
            if nums[n-index-1]==0:
                suffix = 1
        
        return maxProd