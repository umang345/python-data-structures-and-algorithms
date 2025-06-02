from typing import *
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        vis = []
        for _ in range(rows):
            vis.append([False]*cols)
        
        queue = deque()

        for index in range(cols):
            if board[0][index] == 'O':
                queue.append((0,index))
                vis[0][index] = True
            if rows>1 and board[-1][index] == 'O':
                queue.append((rows-1, index))
                vis[rows-1][index] = True
        
        for index in range(1,rows-1):
            if board[index][0] == 'O':
                queue.append((index,0))
                vis[index][0] = True
            if cols>1 and board[index][-1] == 'O':
                queue.append((index, cols-1))
                vis[index][cols-1] = True

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            x,y = queue.popleft()
            for _x,_y in dirs:
                nextx = x+_x
                nexty = y+_y
                if nextx>=0 and nextx<rows and nexty>=0 and nexty<cols:
                    if board[nextx][nexty] == 'O' and not vis[nextx][nexty]:
                        vis[nextx][nexty] = True
                        queue.append((nextx,nexty))

        for rowIndex in range(rows):
            for colIndex in range(cols):
                if board[rowIndex][colIndex]=='O' and not vis[rowIndex][colIndex]:
                    board[rowIndex][colIndex] = 'X'


        '''
        [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
        '''
            

        
        