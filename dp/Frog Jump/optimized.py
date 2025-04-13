from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:

    return helper(n, heights, [-1]*(n+1))

def helper(n:int, heights: list[int], dp:list[int]) -> int:

    if n==0 or n==1:
        return 0

    if n==2:
        return abs(heights[0] - heights[1])

    if dp[n]!=-1:
        return dp[n]

    dp[n] = min(
        abs(heights[n-1]-heights[n-2]) + helper(n-1, heights, dp),
        abs(heights[n-1]-heights[n-3]) + helper(n-2, heights, dp)
    )

    return dp[n]