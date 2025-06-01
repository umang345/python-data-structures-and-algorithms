from typing import *
from collections import Counter 
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        maxHeap = [(-value, key) for key, value in freq.items()]

        heapq.heapify(maxHeap)

        result = []
        while len(result)<k:
            _,key = heapq.heappop(maxHeap)
            result.append(key)
        
        return result