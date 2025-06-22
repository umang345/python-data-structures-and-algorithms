from typing import *

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        xor = 0
        for num1 in nums:
            for num2 in nums:
                xor = max(xor, num1^num2)
        
        return xor