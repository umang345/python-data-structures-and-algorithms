from typing import List
from functools import reduce

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    total = reduce(lambda acc,x : acc+x, arr, 0)

    cache = [[False for totalIndex in range(total+1)] for index in range(len(arr)+1)]

    for index in range(len(arr)+1):
        cache[index][0] = True

    for index in range(1, len(arr)+1):
        for target in range(1,total+1):
            if arr[index-1] > target:
                cache[index][target] = cache[index-1][target]
            else:
                cache[index][target] = cache[index-1][target - arr[index-1]] or cache[index-1][target]
        
    
    for index in range(total//2, -1,-1):
        if cache[len(arr)][index]:
            div1 = index 
            div2 = total - div1 
            return abs(div1 - div2)