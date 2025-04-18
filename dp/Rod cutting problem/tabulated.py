from sys import stdin
import sys

def cutRod(price, n):
    cache = [[-1 for colIndex in range(n+1)] for rowIndex in range(n+1)]
    
    for index in range(n+1):
        cache[index][0] = 0
        cache[0][index] = 0

    for currentSize in range(1, n+1):
        for sizeAvl in range(1, n+1):
            
            if currentSize > sizeAvl:
                cache[currentSize][sizeAvl] = cache[currentSize-1][sizeAvl]
            else:
                cache[currentSize][sizeAvl] = max(
                    cache[currentSize][sizeAvl - currentSize] + price[currentSize-1],
                    cache[currentSize-1][sizeAvl]
                )

    return cache[n][n]