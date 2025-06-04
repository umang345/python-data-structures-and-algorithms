from typing import *
from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid), len(grid[0])
        vis = []
        for _ in range(rows):
            vis.append([False]*cols)

        queue = deque()

        for index in range(cols):
            if grid[0][index] == 1:
                vis[0][index] = True
                queue.append((0,index))
            if rows>1 and grid[-1][index]==1:
                vis[rows-1][index] = True
                queue.append((rows-1, index))

        for index in range(1, rows-1):
            if grid[index][0] == 1:
                vis[index][0] = True
                queue.append((index,0))
            if cols>1 and grid[index][-1]==1:
                vis[index][cols-1] = True
                queue.append((index, cols-1))
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            x,y = queue.popleft()
            for _x, _y in dirs:
                nextx = x+_x
                nexty = y+_y
                if nextx>=0 and nextx<rows and nexty>=0 and nexty<cols:
                    if grid[nextx][nexty] == 1 and not vis[nextx][nexty]:
                        vis[nextx][nexty] = True
                        queue.append((nextx, nexty))

        count = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1 and not vis[row][col]:
                    count+=1
        
        return count