class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if len(obstacleGrid)==0:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[-1 for colIndex in range(cols)] for rowIndex in range(rows)]

        return self.helper(rows-1, cols-1, obstacleGrid,dp)
    
    def helper(self, row, col, grid,dp):
        if row<0 or col<0 or grid[row][col]==1:
            return 0

        if row == 0 and col ==0:
            return 1
        
        if dp[row][col]!=-1:
            return dp[row][col]

        dp[row][col] = self.helper(row-1, col, grid,dp)+self.helper(row, col-1, grid,dp)
        return dp[row][col]