from typing import List

def findWays(arr: List[int], k: int) -> int:
    return helper(len(arr)-1, k, arr)

def helper(index:int, target:int, arr:List[int]) -> int:

    if target == 0:
        return 1
    
    if index < 0:
        return 0

    modulo = (10**9)+7

    includedRes = helper(index-1, target-arr[index], arr)
    excludedRes = helper(index-1, target, arr)

    return (includedRes%modulo + excludedRes%modulo)%modulo