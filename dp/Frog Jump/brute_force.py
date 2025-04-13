from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:

    if n==0 or n==1:
        return 0
    
    if n==2:
        return abs(heights[0] - heights[1])

    return min(
        abs(heights[n-1]-heights[n-2])+frogJump(n-1,heights),
        abs(heights[n-1]-heights[n-3])+frogJump(n-2,heights)
    )
