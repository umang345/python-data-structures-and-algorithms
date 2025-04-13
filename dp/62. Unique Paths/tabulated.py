class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for col in range(n+1)] for row in range(m+1)]
        dp[1][1] = 1

        for rowIndex in range(1, m+1):
            for colIndex in range(1,n+1):
                if rowIndex==1 and colIndex==1:
                    continue
                dp[rowIndex][colIndex] = (dp[rowIndex-1][colIndex]+dp[rowIndex][colIndex-1])

        return dp[m][n]
        