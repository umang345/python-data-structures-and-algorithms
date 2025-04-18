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

    cache = [[-1 for colIndex in range(target+1)] for rowIndex in range(n+1)]

    return helper(n, target, arr, cache)

def helper(index:int, target:int, arr:list, cache:list) -> int:

    if index<=0:
        if target == 0:
            return 1
        return 0

    modulo = (10**9)+7

    if cache[index][target]!=-1:
        return cache[index][target]

    excluded = helper(index-1, target, arr, cache) % modulo
    if arr[index-1] <= target:
        included = helper(index-1, target - arr[index-1], arr, cache) % modulo
        cache[index][target] = (included+excluded)%modulo
    else:
        cache[index][target] = excluded

    return cache[index][target] 
