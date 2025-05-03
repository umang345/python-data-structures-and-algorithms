from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = list()
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n):
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue
                for k in range(j+1,n):
                    if k!=j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
        
        return result
    
'''
TC  -> O(nlogn) + O(n^3)
SC  -> O(1)
'''