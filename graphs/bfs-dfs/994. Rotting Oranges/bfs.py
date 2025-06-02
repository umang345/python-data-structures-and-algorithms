from typing import *
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        directions = [(0,1),(0,-1), (1,0), (-1,0)]

        visited = []
        for row in range(rows):
            visited.append([False]*cols)
        
        queue = deque()

        for rowIndex, row in enumerate(grid):
            for cellIndex, cell in enumerate(row):
                if cell==2:
                    queue.append((rowIndex, cellIndex,0))

        minutes = 0
        while queue:
            currLen = len(queue)
            while currLen>0:
                currLen-=1
                row, col, currMin = queue.popleft()
                if visited[row][col]:
                    continue
                minutes = max(minutes, currMin)
                visited[row][col] = True
                for dirx, diry in directions:
                    x = row+dirx
                    y = col+diry
                    if x>=0 and x<rows and y>=0 and y<cols:
                        if grid[x][y]>0:
                            grid[x][y] = 2
                            queue.append((x,y,currMin+1))

        for row in grid:
            for cell in row:
                if cell == 1:
                    return -1
        
        return minutes


