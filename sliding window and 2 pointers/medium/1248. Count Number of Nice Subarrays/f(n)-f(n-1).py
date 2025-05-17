from typing import *

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.numberOfSubarraysWithAtmostKOddNumbers(nums,k) - self.numberOfSubarraysWithAtmostKOddNumbers(nums,k-1)

    def numberOfSubarraysWithAtmostKOddNumbers(self, nums:List[int], k:int) -> int:
        count = 0
        start = 0
        oddCount = 0

        for end in range(len(nums)):
            if nums[end]%2 != 0:
                oddCount+=1
            
            while oddCount>k and start<=end:
                if nums[start]%2!=0:
                    oddCount-=1
                start+=1
            
            count+=(end-start+1)
        
        return count