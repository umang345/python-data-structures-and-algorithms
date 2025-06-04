from typing import *
from collections import deque

def distinctIsland(arr,n,m) :
    
    vis = []
    for _ in range(n):
        vis.append([False]*m)

    islandSet = set()

    for rowIndex in range(n):
        for colIndex in range(m):
            if not vis[rowIndex][colIndex] and arr[rowIndex][colIndex]==1:
                island = bfs(arr, n,m,rowIndex, colIndex, vis)
                islandSet.add(island)
    
    return len(islandSet)

def bfs(graph,n,m, x,y, vis):

    queue = deque()
    
    queue.append((x,y))
    base = (x,y)
    vis[x][y] = True
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    traversal = []

    while queue:
        currx, curry = queue.popleft()
        traversal.append((currx-base[0], curry-base[1]))
        for dx, dy in dirs:
            nextx, nexty = currx+dx, curry+dy 
            if nextx>=0 and nextx<n and nexty>=0 and nexty<m:
                if graph[nextx][nexty]==1 and not vis[nextx][nexty]:
                    vis[nextx][nexty] = True 
                    queue.append((nextx, nexty))
    
    return tuple(traversal)
