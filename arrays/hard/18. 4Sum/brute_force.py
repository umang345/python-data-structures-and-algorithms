from typing import *

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        result = []
        n = len(nums)
        for a in range(n):
            if a!=0 and nums[a]==nums[a-1]:
                continue
            for b in range(a+1, n):
                if b!=a+1 and nums[b]==nums[b-1]:
                    continue
                for c in range(b+1,n):
                    if c!=b+1 and nums[c]==nums[c-1]:
                        continue
                    for d in range(c+1, n):
                        if d!=c+1 and nums[d]==nums[d-1]:
                            continue
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            result.append([nums[a], nums[b], nums[c], nums[d]])

        return result
    
    
    

'''
TC  ->   O(nlogn)  +  O(n^4)
SC  ->   O(1)
'''