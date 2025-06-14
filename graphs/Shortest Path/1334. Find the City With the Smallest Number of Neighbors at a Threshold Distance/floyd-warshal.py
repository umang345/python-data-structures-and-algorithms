from typing import *
from math import *

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = []
        for _ in range(n):
            graph.append([inf for node in range(n)])
        
        for i in range(n):
            graph[i][i] = 0
        
        for edge in edges:
            u,v,w = edge
            graph[u][v], graph[v][u] = w,w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

        maxNodesVis = n+1
        resultNode = -1

        for node in range(n):
            count = 0
            for adj in range(n):
                if graph[node][adj] <= distanceThreshold:
                    count+=1
            
            if count <= maxNodesVis:
                maxNodesVis = count
                resultNode = node
            
        return resultNode

        