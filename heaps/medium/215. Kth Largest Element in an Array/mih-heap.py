from typing import *
from collections import Counter
import heapq

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False

        freq = Counter(nums)
        minHeap = [num for num in freq.keys()]
        heapq.heapify(minHeap)

        while minHeap:
            minElement = minHeap[0]
            if freq[minElement] == 0:
                heapq.heappop(minHeap)
                continue 
            for index in range(k):
                if freq.get(minElement+index) is None or freq[minElement+index]==0 :
                    return False
                freq[minElement+index]-=1

        return True
        