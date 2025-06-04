from typing import *
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = []
        for _ in range(numCourses):
            graph.append(list())
        
        indegree = [0]*numCourses
        for p in prerequisites:
            graph[p[1]].append(p[0])
            indegree[p[0]]+=1
        
        queue = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for adj in graph[node]:
                indegree[adj]-=1
                if indegree[adj]==0:
                    queue.append(adj)
        
        if len(result)!=numCourses:
            return []
        
        return result