from collections import deque

class Solution:
    
    def topoSort(self, V, edges):
        
        stack = deque()
        graph = []
        for _ in range(V):
            graph.append(list())
        
        for e in edges:
            graph[e[0]].append(e[1])
            
        vis = [False]*V
        for node in range(V):
            if not vis[node]:
                self.topo(node, vis, stack,graph)
        
        result = []
        while stack:
            result.append(stack.pop())
        
        return result
    
    def topo(self, node, vis, stack, graph):
        vis[node] = True
        
        for adj in graph[node]:
            if not vis[adj]:
                self.topo(adj, vis, stack, graph)
        
        stack.append(node)