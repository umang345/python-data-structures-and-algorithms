from sys import stdin
import sys

def cutRod(price, n):
    cache = [[-1 for colIndex in range(n+1)] for rowIndex in range(n+1)]
    return helper(n, n, price, cache)

def helper(currentSize:int,sizeAvl:int, price:list, cache:list) -> int:
    if currentSize<=0 or sizeAvl==0:
        return 0
    
    if cache[currentSize][sizeAvl]!=-1:
        return cache[currentSize][sizeAvl]

    if currentSize > sizeAvl:
        cache[currentSize][sizeAvl] = helper(currentSize-1, sizeAvl, price, cache)
    else:
        cache[currentSize][sizeAvl] = max(
            helper(currentSize, sizeAvl-currentSize, price, cache) + price[currentSize-1],
            helper(currentSize-1, sizeAvl, price, cache)
        ) 
    
    return cache[currentSize][sizeAvl]