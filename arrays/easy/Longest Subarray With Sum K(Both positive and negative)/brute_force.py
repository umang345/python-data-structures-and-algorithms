from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: list, k: int) -> int:
    
    n = len(nums)
    maxLen = 0
    for startIndex in range(n):
        currSum = 0
        end = startIndex
        while end < n:
            currSum = currSum+nums[end]
            if currSum == k:
                currLen = end-startIndex+1
                if maxLen < currLen:
                    maxLen = currLen
            end+=1
    
    return maxLen