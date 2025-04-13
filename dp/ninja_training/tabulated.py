from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    if n == 0:
        return 0

    dp = [[-1 for inner in range(3)] for index in range(n+1)]
    dp[0][0],dp[0][1],dp[0][2] = 0,0,0

    for index in range(1, n+1):
        
        dp[index][0] = points[index-1][0]+max(dp[index-1][1], dp[index-1][2])
        dp[index][1] = points[index-1][1]+max(dp[index-1][0], dp[index-1][2])
        dp[index][2] = points[index-1][2]+max(dp[index-1][0], dp[index-1][1])

    return max(
        dp[n][0],
        max(
            dp[n][1],dp[n][2]
        )
    )