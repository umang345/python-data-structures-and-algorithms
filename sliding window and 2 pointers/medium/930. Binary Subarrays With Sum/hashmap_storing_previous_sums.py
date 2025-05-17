from typing import *

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashMap = dict()
        currSum = 0
        count = 0
        hashMap[0] = 1

        for index, val in enumerate(nums):
            currSum+=val
            '''
            x  = currSum - goal
            '''
            count += hashMap.get(currSum - goal,0)
            hashMap[currSum] = hashMap.get(currSum,0)+1

        return count    