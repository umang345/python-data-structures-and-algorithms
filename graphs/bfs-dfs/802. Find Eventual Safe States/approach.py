from typing import *

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
         
        n = len(graph)

        vis = [False]*n
        pathVis = [False]*n

        result = [True]*n
        for node in range(n):
            if not vis[node]:
                traversedNodes = []
                if self.isCycle(node, vis, pathVis, graph, traversedNodes):
                    for t in traversedNodes:
                        result[t] = False
        safeNodes = []
        for index, isSafe in enumerate(result):
            if isSafe:
                safeNodes.append(index)
        
        return safeNodes

    def isCycle(self, node, vis, pathVis,graph, traversedNodes)->bool:
        vis[node]=True
        traversedNodes.append(node)
        pathVis[node] = True

        for adj in graph[node]:
            if not vis[adj]:
                if self.isCycle(adj, vis, pathVis, graph, traversedNodes):
                    return True
            elif pathVis[adj]:
                return True

        pathVis[node] = False
        traversedNodes.pop()
        return False