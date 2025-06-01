import heapq
from typing import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        pq = []
        for index in range(k):
            heapq.heappush(pq, (nums[index], nums[index]))
        
        for index in range(k, len(nums)):
            heapq.heappush(pq, (nums[index], nums[index]))
            heapq.heappop(pq)
        
        _, res = heapq.heappop(pq)
        return res