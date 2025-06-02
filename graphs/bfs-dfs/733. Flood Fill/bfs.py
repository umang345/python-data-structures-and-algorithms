from typing import *
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        rows, cols = len(image), len(image[0])

        queue = deque()
        queue.append((sr,sc))
        visited = []
        directions = [(0,-1),(0,1),(-1,0),(1,0)]

        for _ in range(rows):
            visited.append([False]*cols)

        while queue:
            x,y = queue.popleft()
            if visited[x][y]:
                continue
            
            visited[x][y] = True
            image[x][y] = color
            for dirx, diry in directions:
                nextx = x+dirx
                nexty = y+diry
                if nextx>=0 and nextx<rows and nexty>=0 and nexty<cols:
                    if image[nextx][nexty] == originalColor:
                        queue.append((nextx, nexty))
        
        return image
