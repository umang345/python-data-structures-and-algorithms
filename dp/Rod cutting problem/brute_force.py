from sys import stdin
import sys

def cutRod(price, n):
    return helper(n, n, price)

def helper(currentSize:int,sizeAvl:int, price:list) -> int:
    if currentSize<=0 or sizeAvl==0:
        return 0

    if currentSize > sizeAvl:
        return helper(currentSize-1, sizeAvl, price)
    else:
        return max(
            helper(currentSize, sizeAvl-currentSize, price) + price[currentSize-1],
            helper(currentSize-1, sizeAvl, price)
        ) 
    