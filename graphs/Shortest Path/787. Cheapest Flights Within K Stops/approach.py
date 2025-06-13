from typing import *
from math import *
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = dict()
        for node in range(n):
            graph[node] = list()
        
        for flight in flights:
            u,v,p = flight
            graph[u].append((v,p))

        dis = [inf]*n
        dis[src] = 0

        pq = [(0,src,0)]

        while pq:
            currStop,node, currDis = heapq.heappop(pq)
            if currStop == k+1:
                continue
            
            for nextNode, edgeDis in graph[node]:
                if currDis+edgeDis < dis[nextNode]:
                    dis[nextNode] = currDis+edgeDis
                    heapq.heappush(pq, (currStop+1, nextNode, dis[nextNode]))

        if dis[dst] == inf:
            return -1

        return dis[dst] 