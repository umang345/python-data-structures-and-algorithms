'''
We will take element with highest frequency at any step
So, 
Keep elements and frequency in max heap

use a queue to keep track when the same element will be available again to add in heap

Since there are only 26 letters, 
TC will be Nlog26  which is almost O(n)
'''
from typing import *
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        maxHeap = []
        freqMap = Counter(tasks)
        
        queue = deque()
        for task in freqMap.keys():
            queue.append((-freqMap[task], 1))

        currTime = 0
        while len(maxHeap)>0 or len(queue)>0:
            currTime+=1
            while queue and queue[0][1] <= currTime:
                remainingCount, _ = queue.popleft()
                heapq.heappush(maxHeap, remainingCount)
            
            if maxHeap:
                currCount = heapq.heappop(maxHeap)
                remainingCount = currCount+1
                if remainingCount!=0:
                    queue.append((remainingCount, currTime+n+1))
        
        return currTime