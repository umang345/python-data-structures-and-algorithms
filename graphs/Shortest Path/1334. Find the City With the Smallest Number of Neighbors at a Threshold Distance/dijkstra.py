from typing import *
from math import *
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        graph = dict()
        for node in range(n):
            graph[node] = list()
        
        for edge in edges:
            u,v,w = edge
            graph[u].append((v,w))
            graph[v].append((u,w))

        maxCity = n+1
        resultNode = -1

        for node in range(n):
            dis = self.dijkstra(n, graph, node)
            count = 0
            for d in dis:
                if d<=distanceThreshold:
                    count+=1
            
            if count <= maxCity:
                maxCity = count
                resultNode = node
        
        return resultNode

    def dijkstra(self, n:int, graph:dict, src:int) -> List[int]:

        dis = [inf]*n
        dis[src] = 0

        pq = [(0,src)]

        while pq:
            currDis, currNode = heapq.heappop(pq)

            for adjNode, adjDis in graph[currNode]:
                if currDis+adjDis < dis[adjNode]:
                    dis[adjNode] = currDis+adjDis
                    heapq.heappush(pq, (dis[adjNode], adjNode))
        
        return dis
        