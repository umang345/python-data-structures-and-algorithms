from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        count=0
        for row in range(n):
            currSum = 0
            for col in range(row, n):
                currSum+=nums[col]
                if currSum==k:
                    count+=1

        return count