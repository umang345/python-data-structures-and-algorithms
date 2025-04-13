class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for col in range(n+1)] for row in range(m+1)]
        return self.helper(m,n,dp)

    def helper(self, row:int, col:int, dp:list[list[int]]) -> int:
        if row == 1 and col == 1:
            return 1
        if row<1 or col<1:
            return 0

        if dp[row][col]!=-1:
            return dp[row][col]

        dp[row][col] = self.helper(row-1, col, dp) + self.helper(row, col-1, dp)
        return dp[row][col]