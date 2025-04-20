from typing import *

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        subsets = [1 for index in range(len(nums))]
        indexCache = [index for index in range(len(nums))]

        for index in range(len(nums)):
            for compare in range(index):
                if nums[index]%nums[compare]==0 and subsets[index] <= subsets[compare]:
                    subsets[index] = subsets[compare]+1
                    indexCache[index] = compare

        largestSubset = []
        largestSubsetLen = 0
        for index in range(len(nums)):
            if subsets[index] > largestSubsetLen:
                largestSubsetLen = subsets[index]
                largestSubset = self.getSequenceFromIndexCache(index, nums, indexCache)
        
        return largestSubset
    
    def getSequenceFromIndexCache(self, index:int, nums:list, indexCache:list):
        seq = [nums[index]]
        while indexCache[index]!=index:
            seq.append(nums[indexCache[index]])
            index = indexCache[index]
        
        return list(reversed(seq))