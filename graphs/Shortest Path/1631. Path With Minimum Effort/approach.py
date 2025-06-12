from typing import *
from math import *
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows, cols = len(heights), len(heights[0])

        effort = []
        for _ in range(rows):
            effort.append([inf for _ in range(cols)])

        effort[0][0] = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        pq = []
        heapq.heappush(pq,(0,0,0))

        ''' (effort, x, y) '''
        
        while pq:

            eff, x, y = heapq.heappop(pq)
            # This eff is the max difference in current path

            if x==rows-1 and y==cols-1:
                return eff
            
            for _x, _y in dirs:
                nx = x+_x
                ny = y+_y
                if nx>=0 and nx<rows and ny>=0 and ny<cols:
                    currDif = abs(heights[nx][ny] - heights[x][y])
                    # The difference between current cell and neighbour
                    currEffort = max(eff, currDif)
                    #  get max difference between cells in current path
                    if currEffort < effort[nx][ny]:
                        effort[nx][ny] = currEffort 
                        heapq.heappush(pq, (effort[nx][ny], nx, ny))
        
        return effort[rows-1][cols-1]