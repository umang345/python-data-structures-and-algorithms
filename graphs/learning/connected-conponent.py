class Solution:
    # Function to return connected components of the graph
    def getComponents(self, V, edges):
        graph = []
        for _ in range(V):
            graph.append([])
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        vis = [False]*V
        result = []
        
        for node in range(V):
            if not vis[node]:
                traversal = []
                self.dfs(node, graph, vis, traversal)
                result.append(traversal)
        
        return result
    
    def dfs(self,node, graph, vis, traversal):
        if vis[node]:
            return
        vis[node] = True
        traversal.append(node)
        for neighbour in graph[node]:
            self.dfs(neighbour, graph, vis, traversal)
    
                