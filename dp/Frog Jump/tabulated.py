from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:

    if n==0 or n==1:
        return 0
    
    if n==2:
        return abs(heights[0]-heights[1])

    dp = [-1]*(n+1)
    dp[0],dp[1],dp[2] = 0,0,abs(heights[0]-heights[1])

    for index in range(3, n+1):
        dp[index] = min(
            abs(heights[index-1]-heights[index-2]) + dp[index-1],
            abs(heights[index-1]-heights[index-3]) + dp[index-2]
        )

    return dp[n]