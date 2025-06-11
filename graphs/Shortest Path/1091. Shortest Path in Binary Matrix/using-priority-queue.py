from typing import *
from math import *
import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if grid[0][0]==1 or grid[rows-1][cols-1]==1:
            return -1
        
        dis = list()
        for _ in range(rows):
            dis.append([inf for _ in range(cols)])

        pq = list()
        dis[0][0] = 1
        ''' PQ -> (dis, row, col) '''
        heapq.heappush(pq, (1, 0 ,0))
        dir = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1),(-1,-1),(-1,1)]

        while pq:
            _,x,y = heapq.heappop(pq)
            
            for _x, _y in dir:
                nx = x+_x
                ny = y+_y
                if nx>=0 and nx<rows and ny>=0 and ny<cols and grid[nx][ny]==0:
                    if dis[x][y] + 1 < dis[nx][ny]:
                        dis[nx][ny] = dis[x][y] + 1
                        heapq.heappush(pq, (dis[nx][ny], nx, ny)) 

        if dis[rows-1][cols-1] == inf:
            return -1
        return dis[rows-1][cols-1]