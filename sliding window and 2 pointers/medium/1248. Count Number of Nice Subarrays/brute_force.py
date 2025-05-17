from typing import *

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        count = 0
        for startIndex in range(len(nums)):
            oddCount = 0
            for index in range(startIndex, len(nums)):
                if nums[index]%2!=0:
                    oddCount+=1
                if oddCount == k:
                    count+=1
                if oddCount > k:
                    break
        
        return count