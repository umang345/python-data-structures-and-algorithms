from typing import *

'''
O(n + n)
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        [1,1,1,0,0,0,1,1,1,1,0]
        '''

        start, end = 0,0
        maxLen = 0
        currZerosInSubarray = 0

        while end < len(nums):
            if nums[end] == 0:
                currZerosInSubarray+=1
                if currZerosInSubarray > k:
                    while start<=end and currZerosInSubarray > k:
                        if nums[start] == 0:
                            currZerosInSubarray-=1
                        start+=1
            
            currLen = end-start+1
            maxLen = max(currLen, maxLen)
            end+=1
        
        return maxLen