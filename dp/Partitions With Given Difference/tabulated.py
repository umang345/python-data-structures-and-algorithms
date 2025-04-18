from os import *
from sys import *
from collections import *
from math import *

from typing import List


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    total = 0
    for num in arr:
        total+=num 
    
    if (total+d) % 2!=0:
        return 0
    target = (total+d)//2

    cache = [[0 for colIndex in range(target+1)] for rowIndex in range(n+1)]

    for rowIndex in range(n+1):
        cache[rowIndex][0] = 1

    modulo = (10**9)+7

    for rowIndex in range(1, n+1):
        for colIndex in range(target+1):
            excluded = cache[rowIndex-1][colIndex]%modulo 
            if arr[rowIndex-1] <= colIndex:
                included = cache[rowIndex-1][colIndex - arr[rowIndex-1]]%modulo 
                cache[rowIndex][colIndex] = (included+excluded)%modulo
            else:
                cache[rowIndex][colIndex] = excluded
    
    return cache[n][target]