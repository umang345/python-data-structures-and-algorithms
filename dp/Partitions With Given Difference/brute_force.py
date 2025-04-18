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

    return helper(n, target, arr)

def helper(index:int, target:int, arr:list) -> int:

    if index<=0:
        if target == 0:
            return 1
        return 0

    modulo = (10**9)+7

    result = -1
    excluded = helper(index-1, target, arr) % modulo
    if arr[index-1] <= target:
        included = helper(index-1, target - arr[index-1], arr) % modulo
        result = (included+excluded)%modulo
    else:
        result = excluded

    return result 