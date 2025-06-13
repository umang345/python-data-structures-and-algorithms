#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        
        inf = 100000000
        
        dis = [inf]*V
        dis[src] = 0
        
        for _ in range(V-1):
            for edge in edges:
                u,v,w = edge
                if dis[u]!=inf and dis[u]+w < dis[v]:
                    dis[v] = dis[u]+w
        
        for edge in edges:
            u,v,w = edge
            if dis[u]!=inf and dis[u]+w < dis[v]:
                return [-1]
        
        return dis