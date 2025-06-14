from typing import List
import heapq

'''
Time complexity -> O(ElogE)
'''

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, graph: List[List[int]]) -> int:
        
        vis = [False]*V
        mstSum = 0
        
        pq = [(0,0,-1)]  
        ''' (weight, node, parent) '''
        
        while pq:
            w,node,parent = heapq.heappop(pq)
            
            if vis[node]:
                continue
            
            vis[node] = True
            mstSum+=w
            
            for adjNode, adjW in graph[node]:
                if not vis[adjNode]:
                    heapq.heappush(pq,(adjW, adjNode, node))
                    
        return mstSum
        