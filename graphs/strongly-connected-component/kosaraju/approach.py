from collections import deque
from typing import *

class Solution:

    def kosaraju(self, adj):
        
        n = len(adj)
        stack = deque()
        vis = [False]*n
        
        for node in range(n):
            if not vis[node]:
                self.dfsWithStack(adj, vis, stack, node)
        
        revGraph = self.getReversedGraph(adj)
        
        count = 0
        vis = [False]*n
        
        while stack:
            node = stack.pop()
            if not vis[node]:
                count+=1
                self.dfs(revGraph, vis, node)
        
        return count
                
        
    def getReversedGraph(self, graph:List[List[int]]) -> List[List[int]]:
        n = len(graph)
        revGraph = []
        for _ in range(n):
            revGraph.append(list())
        
        for u in range(n):
            for v in graph[u]:
                revGraph[v].append(u)
        
        return revGraph
    
    def dfs(self, graph:List[List[int]], vis:List[bool], node:int):
        vis[node] = True
        for adj in graph[node]:
            if not vis[adj]:
                self.dfs(graph, vis, adj)
        
    
    def dfsWithStack(self, graph:List[List[int]], vis:List[bool],stack:deque, node:int):
        vis[node] = True
        for adj in graph[node]:
            if not vis[adj]:
                self.dfsWithStack(graph, vis,stack, adj)
        
        stack.append(node)
        