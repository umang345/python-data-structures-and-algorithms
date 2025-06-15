#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        
        vis = [False]*V
        currTime = [0]
        inTime = [0]*V
        lowTime = [0]*V
        points = [False]*V
        
        self.helper(adj, vis, 0, -1, currTime, inTime, lowTime, points)
        
        result = []
        for node in range(V):
            if points[node]:
                result.append(node)
        
        if len(result)==0:
            result.append(-1)
        return result
        
        
    def helper(self, graph, vis, node, parent, currTime, inTime, lowTime, points):
        
        vis[node] = True
        currTime[0]+=1
        inTime[node] = currTime[0]
        lowTime[node] = currTime[0]
        
        child = 0
        for adjNode in graph[node]:
            if adjNode == parent or adjNode == node:
                continue
            
            if vis[adjNode]:
                lowTime[node] = min(lowTime[node], inTime[adjNode])
            else:
                child+=1
                self.helper(graph, vis, adjNode, node, currTime, inTime, lowTime, points)
                lowTime[node] = min(lowTime[node], lowTime[adjNode])
                if inTime[node] <= lowTime[adjNode] and parent!=-1:
                    points[node] = True
                    
        if child>1 and parent==-1:
            points[node] = True
            