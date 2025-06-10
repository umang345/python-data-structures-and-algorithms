from typing import List
from math import *
from collections import deque

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        
        graph = dict()
        for node in range(V):
            graph[node] = list()
            
        for edge in edges:
            u,v,d = edge
            graph[u].append((v,d))
        
        dis = [inf]*V
        vis = [False]*V
        stack = deque()
        
        self.helper(graph, 0, vis,stack)
        
        dis[0] = 0
        while stack:
            node = stack.pop()
            for adj in graph[node]:
                if dis[node] + adj[1] < dis[adj[0]]:
                    dis[adj[0]] = dis[node] + adj[1] 
        
        
        for index in range(V):
            if dis[index] == inf:
                dis[index] = -1
        
        return dis
    
    def helper(self, graph, node, vis, stack):
        vis[node] = True
        
        for adj in graph[node]:
            if not vis[adj[0]]:
                self.helper(graph, adj[0], vis, stack)
        
        stack.append(node)

    
        
