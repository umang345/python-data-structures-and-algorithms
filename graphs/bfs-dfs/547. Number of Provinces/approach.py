from typing import *

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        visited = [False]*n

        provinces = 0

        for city in range(n):
            if not visited[city]:
                provinces+=1
                self.dfs(city, isConnected, visited)
        
        return provinces
    
    def dfs(self, node, graph, visited):
        if visited[node]:
            return
        visited[node] = True
        for neighbour in graph[node]:
            for nextNode in range(len(graph)):
                if nextNode!=node and graph[node][nextNode]==1:
                    self.dfs(nextNode, graph, visited)
