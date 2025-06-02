from typing import *
from collections import deque 

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        vis = []
        result = []
        for _ in range(rows):
            vis.append([False]*cols)
            result.append([0]*cols)
        
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    vis[row][col] = True
                    queue.append((row, col, 0))
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            x,y,dis = queue.popleft()
            result[x][y] = dis
            for nx, ny in dirs:
                nextx = x+nx
                nexty = y+ny
                if nextx>=0 and nextx<rows and nexty>=0 and nexty<cols and not vis[nextx][nexty]:
                    vis[nextx][nexty] = True
                    queue.append((nextx, nexty, dis+1))

        return result
    