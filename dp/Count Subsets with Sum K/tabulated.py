from typing import List

def findWays(arr: List[int], k: int) -> int:
    cache = [[0 for target in range(k+1)] for index in range(len(arr)+1)]
    for rowIndex in range(len(arr)+1):
        cache[rowIndex][0] = 1

    modulo = (10**9)+7

    for row in range(1,len(arr)+1):
        for amt in range(1, k+1):
            if arr[row-1] > amt:
                cache[row][amt] = cache[row-1][amt]
            else:
                included = cache[row-1][amt-arr[row-1]]%modulo
                excluded = cache[row-1][amt]%modulo
                cache[row][amt] = (included+excluded)%modulo 

    return cache[len(arr)][k]