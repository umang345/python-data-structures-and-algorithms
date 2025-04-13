class Solution:
    def climbStairs(self, n: int) -> int:
        
        return self.helper(n, [-1]*(n+1))

    def helper(self, n, dp) -> int:
        if n<0:
            return 0
        if n==0 or n==1:
            return 1

        if dp[n]!=-1:
            return dp[n]
        
        dp[n] = self.helper(n-1,dp) + self.helper(n-2, dp)
        return dp[n]
