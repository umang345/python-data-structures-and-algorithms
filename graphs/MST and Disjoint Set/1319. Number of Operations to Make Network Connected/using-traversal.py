from typing import *

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < (n-1):
            return -1

        graph = dict()
        for node in range(n):
            graph[node] = list()

        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        vis = [False]*n

        count = -1
        for node in range(n):
            if not vis[node]:
                count+=1
                self.dfs(node, vis, graph)
        
        return count
    
    def dfs(self, node:int, vis:List[bool], graph:dict):
        vis[node] = True 

        for adj in graph[node]:
            if not vis[adj]:
                self.dfs(adj, vis, graph)
        