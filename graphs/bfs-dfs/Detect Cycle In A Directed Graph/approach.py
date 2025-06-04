class Solution:
    def isCycle(self, v, edges):
        graph = []
        for _ in range(v):
            graph.append(list())
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
        
        vis = [False]*v
        pathVis = [False]*v
        
        for node in range(v):
            if not vis[node]:
                if self.dfs(node, vis, pathVis, graph):
                    return True
        
        return False
        
    def dfs(self, node, vis, pathVis , graph):
        vis[node] = True
        pathVis[node] = True
        
        for adj in graph[node]:
            if not vis[adj]:
                if self.dfs(adj, vis, pathVis, graph):
                    return True
            elif pathVis[adj]:
                return True
        
        pathVis[node] = False
        return False