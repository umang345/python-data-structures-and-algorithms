from typing import *

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        [1,1,1,0,0,0,1,1,1,1,0]

        '''

        maxLen = 0

        for startIndex in range(len(nums)):
            zerosLeft = k
            currLen = 0
            for index in range(startIndex, len(nums)):
                currLen+=1
                if nums[index] == 0:
                    if zerosLeft > 0:
                        zerosLeft-=1
                    else:
                        break
                
                maxLen = max(currLen, maxLen)
        
        return maxLen