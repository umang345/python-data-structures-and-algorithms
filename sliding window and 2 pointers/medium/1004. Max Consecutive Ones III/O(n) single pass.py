from typing import *

'''
Incrementing left pointer just by 1
O(n)
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        start, end = 0,0
        maxLen = 0
        currZerosInSubarray = 0

        while end < len(nums):
            if nums[end] == 0:
                currZerosInSubarray+=1
            
            if currZerosInSubarray > k:
                if nums[start] == 0:
                    currZerosInSubarray-=1
                start+=1
            
            if currZerosInSubarray <= k:
                currLen = end-start+1
                maxLen = max(currLen, maxLen)
            end+=1
        
        return maxLen