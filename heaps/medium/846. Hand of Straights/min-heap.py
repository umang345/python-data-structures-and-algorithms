from typing import *
import heapq 
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if not len(hand)%groupSize==0:
            return False

        freq = Counter(hand)
        minHeap = [key for key in freq.keys()]
        heapq.heapify(minHeap)

        while minHeap:
            minElement = minHeap[0]
            if freq[minElement]==0:
                heapq.heappop(minHeap)
                continue
            
            for index in range(groupSize):
                if freq.get(minElement+index) is None or freq[minElement+index]==0:
                    return False
                
                freq[minElement+index]-=1
        
        return True