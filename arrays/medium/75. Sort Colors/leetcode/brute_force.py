from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        redCount, whiteCount, blueCount = 0,0,0

        for num in nums:
            if num == 0:
                redCount+=1
            elif num == 1:
                whiteCount+=1
            else:
                blueCount+=1

        currIndex = 0

        while redCount>0:
            nums[currIndex] = 0
            currIndex+=1
            redCount-=1

        while whiteCount>0:
            nums[currIndex] = 1
            currIndex+=1
            whiteCount-=1
        
        while blueCount>0:
            nums[currIndex] = 2
            currIndex+=1
            blueCount-=1
            
        
'''
Time Complexity -> O(n) + O(n)
Space Complexity -> O(1)
'''