from typing import *

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)

        size = [0]*(n*n)
        parent = [node for node in range(n*n)]
        for row in range(n):
            for col in range(n):
                node = (row*n)+col
                if grid[row][col]==1:
                    size[node] = 1

        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    for _x, _y in dirs:
                        nx, ny = row+_x, col+_y
                        adjNode = (nx*n)+ny
                        if nx>=0 and nx<n and ny>=0 and ny<n and grid[nx][ny]==1:
                            adjParent = self.findParent(adjNode, parent)
                            currParent = self.findParent((row*n)+col, parent)
                            if adjParent!=currParent:
                                parent[adjParent] = currParent
                                size[currParent]+=size[adjParent]
        
        result = max(size)
        
        for x in range(n):
            for y in range(n):
                if grid[x][y]==0:
                    temp = set()
                    for _x, _y in dirs:
                        nx, ny = x+_x, y+_y
                        if nx>=0 and nx<n and ny>=0 and ny<n and grid[nx][ny]==1:
                            adjNode = (nx*n)+ny
                            adjParent = self.findParent(adjNode, parent)
                            temp.add(adjParent)
                    
                    currRes = 1
                    for p in temp:
                        currRes+=size[p]
                    
                    result = max(currRes, result)
        
        return result

    def findParent(self, node:int, parent:List[int]) -> int:
        if node == parent[node]:
            return node
        
        parent[node] = self.findParent(parent[node], parent)
        return parent[node]


