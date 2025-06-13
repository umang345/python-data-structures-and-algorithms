from typing import *
from math import *
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        dis = [inf]*n
        graph = dict()
        for index in range(n):
            graph[index] = list()
        
        for time in times:
            u,v,w = time
            graph[u-1].append((v-1,w))
        
        dis[k-1] = 0
        pq = [(0,k-1)]

        while pq:
            currTime, currNode = heapq.heappop(pq)

            for adjNode, adjTime in graph[currNode]:
                if currTime + adjTime < dis[adjNode]:
                    dis[adjNode] = currTime + adjTime
                    heapq.heappush(pq, (currTime + adjTime, adjNode))
        
        minTime = max(dis)
        if minTime == inf:
            return -1
        
        return minTime

