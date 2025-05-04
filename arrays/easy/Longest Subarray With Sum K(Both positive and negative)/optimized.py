from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hashMap = dict()
        currSum = 0
        count=0
        hashMap[0] = 1
        for num in nums:
            currSum+=num
            numToCheck = currSum - k
            if not hashMap.get(numToCheck) is None:
               count+=hashMap[numToCheck]

            hashMap[currSum] = hashMap.get(currSum,0)+1 

        return count