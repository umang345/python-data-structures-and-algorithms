from math import *
from collections import deque

class Solution:
    def shortestPath(self, graph, src):
        
        n = len(graph)
        dis = [inf]*n
        dis[src] = 0
        
        queue = deque()
        queue.append(src)
        
        while queue:
            node = queue.popleft()
            for adj in graph[node]:
                if dis[node]+1 < dis[adj]:
                    dis[adj] = dis[node]+1
                    queue.append(adj)
        
        for index in range(n):
            if dis[index] == inf:
                dis[index] = -1
                
        return dis