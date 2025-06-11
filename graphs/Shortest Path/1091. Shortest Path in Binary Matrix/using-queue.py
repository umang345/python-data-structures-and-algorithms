from typing import *
from math import *
from collections import deque

'''
The implementation using queue is exactly same as using Min-Heap
But we don't need heap and the distance is always increasing by 1
when we are adding it to the queue
So the pairs are always inserted in increasing order of distance

So implementation using queue is faster in this case
'''

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if grid[0][0]==1 or grid[rows-1][cols-1]==1:
            return -1
        
        dis = list()
        for _ in range(rows):
            dis.append([inf for _ in range(cols)])

        queue = deque()
        dis[0][0] = 1
        ''' PQ -> (dis, row, col) '''
        # heapq.heappush(pq, (1, 0 ,0))
        queue.append((1, 0 ,0))
        dir = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1),(-1,-1),(-1,1)]

        while queue:
            _,x,y = queue.popleft()
            
            for _x, _y in dir:
                nx = x+_x
                ny = y+_y
                if nx>=0 and nx<rows and ny>=0 and ny<cols and grid[nx][ny]==0:
                    if dis[x][y] + 1 < dis[nx][ny]:
                        dis[nx][ny] = dis[x][y] + 1
                        queue.append((dis[nx][ny], nx, ny)) 

        if dis[rows-1][cols-1] == inf:
            return -1
        return dis[rows-1][cols-1]