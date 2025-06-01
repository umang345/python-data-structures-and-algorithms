from typing import *
from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False

        freq = Counter(nums)
        while freq:
            minElement = min(freq.keys())
            for index in range(k):
                if freq.get(minElement+index) is None:
                    return False
                freq[minElement+index]-=1
                if freq[minElement+index] == 0:
                    del freq[minElement+index]
            
        return True
        