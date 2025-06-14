from os import *
from sys import *
from collections import *
from math import *
import heapq

def calculatePrimsMST(n, m, g):

    graph = dict()
    for node in range(n):
        graph[node] = list()

    for edge in g:
        u,v,w = edge 
        graph[u-1].append((v-1,w))
        graph[v-1].append((u-1,w))

    mst = []
    vis = [False]*n 

    pq = [(0,0,-1)]
    ''' (weight,node, parent) '''

    while pq:
        w,node,parent = heapq.heappop(pq)

        if vis[node]:
            continue 
        
        vis[node] = True
        if parent!=-1:
            mst.append([node+1, parent+1, w])

        for adjNode,adjW in graph[node]:
            if not vis[adjNode]:
                heapq.heappush(pq,(adjW, adjNode, node))
    
    return mst 