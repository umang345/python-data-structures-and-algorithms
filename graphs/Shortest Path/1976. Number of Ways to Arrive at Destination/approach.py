from typing import *
from math import *
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        graph = dict()
        for node in range(n):
            graph[node] = list()

        for road in roads:
            u,v,time = road
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        ways = [0]*n
        dis = [inf]*n

        ways[0] = 1
        dis[0] = 0

        pq = [(0, 0)]

        while pq:
            currDis, currNode = heapq.heappop(pq)

            for adjNode, adjTime in graph[currNode]:
                if currDis + adjTime == dis[adjNode]:
                    ways[adjNode]= (ways[adjNode] + ways[currNode])%(1e9+7)
                elif currDis + adjTime < dis[adjNode]:
                    dis[adjNode] = currDis + adjTime
                    ways[adjNode] = ways[currNode]
                    heapq.heappush(pq, (dis[adjNode], adjNode))
        
        return int(ways[n-1])