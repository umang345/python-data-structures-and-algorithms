from typing import *

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        goodArray = 0

        for startIndex in range(len(nums)):
            hashSet = set()
            for index in range(startIndex, len(nums)):
                hashSet.add(nums[index])
                if len(hashSet)>k:
                    break
                if len(hashSet)==k:
                    goodArray+=1
        
        return goodArray