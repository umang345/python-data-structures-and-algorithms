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

    prev = 0
    curr = abs(heights[0]-heights[1])

    for index in range(3, n+1):
        computed = min(
            abs(heights[index-1] - heights[index-2]) + curr,
            abs(heights[index-1] - heights[index-3]) + prev
        )

        prev = curr
        curr = computed
    
    return curr
