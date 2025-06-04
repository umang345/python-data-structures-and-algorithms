from collections import deque 
from typing import *

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1]*n

        for node in range(n):
            if colors[node] == -1:
                if not self.bfs(graph, node, colors):
                    return False
        
        return True
    
    def bfs(self, graph, node, colors):
        colors[node] = 0
        queue = deque()

        queue.append((node, 0))
        while queue:
            node, color = queue.popleft()
            for ne in graph[node]:
                if colors[ne]==-1:
                    colors[ne] = 1-color
                    queue.append((ne,1-color))
                elif colors[ne] == color:
                    return False
        
        return True