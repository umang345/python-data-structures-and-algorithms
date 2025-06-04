from typing import *
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = []
        for _ in range(numCourses):
            graph.append(list())
        
        for p in prerequisites:
            graph[p[1]].append(p[0])
        
        vis = [False]*numCourses
        pathVis = [False]*numCourses

        stack = deque()

        for node in range(numCourses):
            if not vis[node]:
                if self.topoDfs(graph, node, vis, pathVis, stack):
                    return []
        
        result = []
        while stack:
            result.append(stack.pop())
        
        return result

    def topoDfs(self, graph:List[List[int]], node:int, vis:List[int], pathVis:List[int], stack:deque) -> bool:

        vis[node] = True
        pathVis[node] = True

        for adj in graph[node]:
            if not vis[adj]:
                if self.topoDfs(graph, adj, vis, pathVis, stack):
                    return True
            elif pathVis[adj]:
                return True

        pathVis[node] = False
        stack.append(node)
        return False
        