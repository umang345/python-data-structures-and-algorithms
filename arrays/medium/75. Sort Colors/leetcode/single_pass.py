from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        redIndex = 0
        blueIndex = len(nums)-1

        currIndex = 0
        while currIndex <= blueIndex:
            if nums[currIndex] == 0:
                nums[redIndex], nums[currIndex] = nums[currIndex], nums[redIndex]
                redIndex+=1
                if currIndex < redIndex:
                    currIndex+=1
            elif nums[currIndex] == 2:
                nums[blueIndex], nums[currIndex] = nums[currIndex], nums[blueIndex]
                blueIndex-=1
            else:
                currIndex+=1


        
        '''
                0  2         
                |  |
        [ 0, 0, 1, 1, 2, 2]


              |     |
        [0,0, 1, 1, 1, 2, 2]

        '''