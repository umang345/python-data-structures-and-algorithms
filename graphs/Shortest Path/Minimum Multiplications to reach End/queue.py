#User function Template for python3

from typing import List
from collections import deque
from math import *

'''
Exact same solution, but this will be a bit faster
because the number of multiplications is increasing by 1
so it automatically gets sorted in queue
'''


class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        
        dis = [inf]*100000                
        dis[start] = 0
        
        
        queue = deque()
        queue.append((0,start))
        
        while queue:
            currMul, currNum = queue.popleft()
            
            if currNum == end:
                return currMul
            
            for num in arr:
                nextMul = (currNum*num)%100000
                if currMul+1 < dis[nextMul]:
                    dis[nextMul] = currMul+1
                    queue.append((currMul+1, nextMul))
            
            
        
        return -1