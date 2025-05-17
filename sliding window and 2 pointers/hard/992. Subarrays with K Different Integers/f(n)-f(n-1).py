from typing import *

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        return self.subarrayWithAtmostKDistinct(nums, k) - self.subarrayWithAtmostKDistinct(nums, k-1)

    def subarrayWithAtmostKDistinct(self, nums:list, k:int) -> int:
        
        count = 0
        start = 0
        hashMap = dict()

        for end in range(len(nums)):
            hashMap[nums[end]] = hashMap.get(nums[end],0)+1
            while len(hashMap.keys()) > k and start<=end:
                hashMap[nums[start]]-=1
                if hashMap[nums[start]]==0:
                    del hashMap[nums[start]]
                start+=1
            
            count+=(end-start+1)
        
        return count
