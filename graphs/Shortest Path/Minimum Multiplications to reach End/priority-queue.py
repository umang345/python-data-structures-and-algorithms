#User function Template for python3

from typing import List
import heapq
from math import *

class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        
        dis = [inf]*100000                
        dis[start] = 0
        
        
        pq = [(0,start)]
        
        while pq:
            currMul, currNum = heapq.heappop(pq)
            
            if currNum == end:
                return currMul
            
            for num in arr:
                nextMul = (currNum*num)%100000
                if currMul+1 < dis[nextMul]:
                    dis[nextMul] = currMul+1
                    heapq.heappush(pq, (currMul+1, nextMul))
            
        return -1