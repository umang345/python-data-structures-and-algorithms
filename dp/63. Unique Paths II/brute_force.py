class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if len(obstacleGrid)==0:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        return self.helper(rows-1, cols-1, obstacleGrid)
    
    def helper(self, row, col, grid):
        if row<0 or col<0 or grid[row][col]==1:
            return 0

        if row == 0 and col ==0:
            return 1

        return self.helper(row-1, col, grid)+self.helper(row, col-1, grid)