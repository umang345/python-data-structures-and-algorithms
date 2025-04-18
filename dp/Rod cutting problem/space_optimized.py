from sys import stdin
import sys

def cutRod(price, n):
    cache = [0 for colIndex in range(n+1)]

    for currentSize in range(1, n+1):
        currentRes = [0 for colIndex in range(n+1)]
        for sizeAvl in range(1, n+1):
            
            if currentSize > sizeAvl:
                currentRes[sizeAvl] = cache[sizeAvl]
            else:
                currentRes[sizeAvl] = max(
                    currentRes[sizeAvl - currentSize] + price[currentSize-1],
                    cache[sizeAvl]
                )
        
        for cacheIndex in range(n+1):
            cache[cacheIndex] = currentRes[cacheIndex]

    return cache[n]