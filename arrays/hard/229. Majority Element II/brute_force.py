from typing import *

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = dict()
        result = []
        for num in nums:
            hashMap[num] = hashMap.get(num,0)+1

        n = len(nums)
        for val, freq in hashMap.items():
            if freq > (n//3):
                result.append(val)
        
        return result
    
'''
Using a hashmap
TC  -> O(n)+O(n)
SC  -> O(n)
'''