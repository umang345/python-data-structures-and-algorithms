from collections import deque

class Solution:
    def isCycle(self, V, edges):
        graph = []
        for _ in range(V):
            graph.append(list())
        
        
        indegree = [0]*V
        for e in edges:
            indegree[e[1]]+=1
            graph[e[0]].append(e[1])
        
        queue = deque()
        for node in range(V):
            if indegree[node] == 0:
                queue.append(node)
        
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for adj in graph[node]:
                indegree[adj]-=1
                if indegree[adj]==0:
                    queue.append(adj)
        
        if len(order)!=V:
            return True
        
        return False
        
        
        
        