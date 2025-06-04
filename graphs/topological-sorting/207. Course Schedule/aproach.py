from typing import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = []
        for _ in range(numCourses):
            graph.append(list())
        
        for p in prerequisites:
            graph[p[1]].append(p[0])
        
        vis, pathVis = [False]*numCourses, [False]*numCourses
        for node in range(numCourses):
            if not vis[node]:
                if self.isCycleDfs(graph, node, vis, pathVis):
                    return False
        
        return True

    def isCycleDfs(self,graph:List[List[int]], node:int, vis:List[bool], pathVis:List[bool]) -> bool:

        vis[node] = True
        pathVis[node] = True

        for adj in graph[node]:
            if not vis[adj]:
                if self.isCycleDfs(graph, adj, vis, pathVis):
                    return True
            elif pathVis[adj]:
                return True

        pathVis[node] = False
        return False