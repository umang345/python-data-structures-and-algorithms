import heapq 
from typing import *

'''
Maintain a min heap of size k always
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = [num for num in nums]
        heapq.heapify(self.minHeap)
        while len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
    
        return self.minHeap[0]