#User function Template for python3

from typing import List
class Solution:
    def numOfIslands(self, n: int, m: int, queries: List[List[int]]) -> List[int]:
        grid = [[0 for _ in range(m)] for _ in range(n)]

        count = 0
        result = []
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        parent = [node for node in range(n*m)]
    
        for x,y in queries:
            if grid[x][y]!=1:
                grid[x][y] = 1
                count+=1
    
                for _x,_y in dirs:
                    nx,ny = x+_x, y+_y 
                    if nx>=0 and nx<n and ny>=0 and ny<m and grid[nx][ny]==1:
                        parentAdj = self.findParent((nx*m)+ny, parent)
                        currNode = (x*m)+y
                        if parentAdj != currNode:
                            parent[parentAdj] = currNode
                            count-=1
                
            result.append(count)
        
        return result
    
    def findParent(self,node, parent):
        if node == parent[node]:
            return node 
        
        parent[node] = self.findParent(parent[node], parent)
        return parent[node]
    
    