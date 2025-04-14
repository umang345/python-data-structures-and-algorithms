from typing import List
from functools import reduce

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    total = reduce(lambda acc,x : acc+x, arr, 0)

    cache = [False for totalIndex in range(total+1)]
    cache[0] = True

    for index in range(1, len(arr)+1):
        current = [False for totalIndex in range(total+1)]
        current[0] = True
        for target in range(1,total+1):
            if arr[index-1] > target:
                current[target] = cache[target]
            else:
                current[target] = cache[target - arr[index-1]] or cache[target]
        
        for target in range(0, total+1):
            cache[target] = current[target]
    
    for index in range(total//2, -1,-1):
        if cache[index]:
            div1 = index 
            div2 = total - div1 
            return abs(div1 - div2)