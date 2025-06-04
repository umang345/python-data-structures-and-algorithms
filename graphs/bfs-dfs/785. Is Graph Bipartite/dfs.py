from typing import *

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1]*n

        for node in range(n):
            if colors[node] == -1:
                if not self.dfs(graph, node, 0, colors):
                    return False
        
        return True
    
    def dfs(self, graph: List[List[int]], node,color, colors) -> bool:
        colors[node] = color
        for neighbour in graph[node]:
            if colors[neighbour] == -1:
                if not self.dfs(graph, neighbour, 1-color, colors):
                    return False
            else:
                if colors[neighbour]==color:
                    return False
        
        return True