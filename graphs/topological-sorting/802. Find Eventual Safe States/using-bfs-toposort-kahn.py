from typing import *
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        revGraph = dict()
        V = len(graph)
        indegree = [0]*V

        for index in range(V):
            revGraph[index] = list()

        for index, vList in enumerate(graph):
            for v in vList:
                revGraph[v].append(index)
                indegree[index]+=1
        
        queue = deque()
        safeNodes = [False] * V

        for node in range(V):
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            safeNodes[node] = True
            for adj in revGraph[node]:
                indegree[adj]-=1
                if indegree[adj]==0:
                    queue.append(adj)
        
        result = []
        for node in range(V):
            if safeNodes[node]:
                result.append(node)
        
        return result