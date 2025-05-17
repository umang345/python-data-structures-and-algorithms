from typing import *

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        [1,2,3,4,5,6,1]  k = 3

        '''

        maxSum = 0
        for index in range(k+1):
            currSum = 0
            for leftIndex in range(0,index):
                currSum+=cardPoints[leftIndex]
            
            for rightIndex in range(len(cardPoints)-1, len(cardPoints)-k+index-1, -1):
                currSum+=cardPoints[rightIndex]
            
            maxSum = max(maxSum, currSum)
        
        return maxSum