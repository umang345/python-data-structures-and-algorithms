class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n<0:
            return 0
        if n==0 or n==1:
            return 1

        dp = [-1] * (n+1)

        dp[0],dp[1] = 1,1
        for index in range(2, n+1):
            dp[index] = dp[index-1]+dp[index-2]
        
        return dp[n]