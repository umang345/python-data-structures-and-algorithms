class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid)==0:
            return 0
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[rows-1][cols-1] == 1:
            return 0

        dp = [[0 for colIndex in range(cols)] for rowIndex in range(rows)]
        for rowIndex in range(rows):
            for colIndex in range(cols):
                if obstacleGrid[rowIndex][colIndex]==0:
                    if rowIndex == 0 and colIndex == 0:
                        dp[rowIndex][colIndex] = 1
                        continue
                    dp[rowIndex][colIndex] = dp[rowIndex-1][colIndex]+dp[rowIndex][colIndex-1]

        return dp[rows-1][cols-1]