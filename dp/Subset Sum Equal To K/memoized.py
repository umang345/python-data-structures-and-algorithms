from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
    return helper(n-1, k, arr, dict())

def helper(index:int, target:int, arr:list[int], cache:dict())->bool:
    if target==0:
        return True 
    
    if index<0:
        return False

    key = f"{index}-{target}"
    if not cache.get(key) is None:
        return cache[key]

    if arr[index] > target:
        cache[key] =  helper(index-1,target, arr, cache)
    else:
        cache[key] = helper(index-1, target-arr[index], arr, cache) or helper(index-1, target, arr, cache)

    return cache[key]
    