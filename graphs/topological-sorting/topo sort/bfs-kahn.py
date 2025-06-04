from collections import deque

class Solution:
    
    def topoSort(self, V, edges):
        
        graph = []
        for _ in range(V):
            graph.append(list())
        
        indegree = [0]*V
        for e in edges:
            graph[e[0]].append(e[1])
            indegree[e[1]]+=1
        
        queue = deque()
        
        for node in range(V):
            if indegree[node] == 0:
                queue.append(node)
        
        ordering = []
        
        while queue:
            node = queue.popleft()
            ordering.append(node)
            for adj in graph[node]:
                indegree[adj]-=1
                if indegree[adj]==0:
                    queue.append(adj)
        
        return ordering
        
        
        