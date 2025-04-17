from typing import List

def findWays(arr: List[int], k: int) -> int:
    cache = [[-1 for target in range(k+1)] for index in range(len(arr))]
    return helper(len(arr)-1, k, arr, cache)

def helper(index:int, target:int, arr:List[int], cache:List[int]) -> int:

    if target == 0:
        return 1
    
    if index < 0 or target < 0:
        return 0

    if cache[index][target] != -1:
        return cache[index][target] 

    modulo = (10**9)+7

    includedRes = helper(index-1, target-arr[index], arr, cache)
    excludedRes = helper(index-1, target, arr, cache)

    cache[index][target] = (includedRes%modulo + excludedRes%modulo)%modulo
    return cache[index][target]