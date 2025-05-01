from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash = dict()
        result = None

        for index,num in enumerate(nums):
            currNumToCheck = target - num
            if not hash.get(currNumToCheck) is None:
                result = [hash[currNumToCheck], index]
                break
            else:
                hash[num] = index

        return result
    

'''
Time Complexity : O(n)  +  [O(1) -> O(n)]
Space Complexity : O(n)
'''