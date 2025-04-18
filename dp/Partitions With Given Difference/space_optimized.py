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

    cache = [0 for colIndex in range(target+1)]

    cache[0]=1
    modulo = (10**9)+7

    for rowIndex in range(1, n+1):
        tempCache = [0 for colIndex in range(target+1)]
        for colIndex in range(target+1):
            excluded = cache[colIndex]%modulo 
            if arr[rowIndex-1] <= colIndex:
                included = cache[colIndex - arr[rowIndex-1]]%modulo 
                tempCache[colIndex] = (included+excluded)%modulo
            else:
                tempCache[colIndex] = excluded
        
        for cacheIndex in range(target+1):
            cache[cacheIndex] = tempCache[cacheIndex]

    return cache[target]