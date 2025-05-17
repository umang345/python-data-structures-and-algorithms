from typing import *

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        [1,2,3,4,5,6,1]  k = 3

        '''

        maxSum = 0
        for index in range(k):
            maxSum+=cardPoints[index]

        left, right = k-1,len(cardPoints)-1

        currSum = maxSum
        while left>=0:
            currSum+=cardPoints[right]
            currSum-=cardPoints[left]
            right-=1
            left-=1
            maxSum = max(maxSum, currSum)
        
        return maxSum