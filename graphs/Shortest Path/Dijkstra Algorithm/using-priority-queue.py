import heapq
from math import *

'''
Time Complexity  ->  O(E * Log(V))
'''

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        graph = dict()
        for node in range(V):
            graph[node] = list()
            
        for edge in edges:
            u,v,d = edge
            graph[u].append((v,d))
            graph[v].append((u,d))
            
        pq = []
        dis = [inf]*V
        dis[src] = 0
        ''' PQ -> (dis , node) '''
        
        heapq.heappush(pq, (0, src))
        
        while pq:
            d,node = heapq.heappop(pq)
            for adj, adjDis in graph[node]:
                if dis[node]+adjDis < dis[adj]:
                    dis[adj] = dis[node]+adjDis
                    heapq.heappush(pq,(dis[adj], adj))
        
        for index in range(V):
            if dis[index] == inf:
                dis[index] = -1
        
        return dis