from functools import *
from math import inf

def findLargestMinDistance(boards:list, k:int):
    
    maxElement = reduce(lambda acc,x : max(acc,x), boards,boards[0])
    totalSum = reduce(lambda acc,x : acc+x, boards,0)

    result = inf
    low,high = maxElement, totalSum
    while low<=high:
        maxTime = low + (high-low)//2
        if helper(boards, k, maxTime):
            result = min(result, maxTime)
            high = maxTime-1
        else:
            low = maxTime+1
    
    return result

def helper(boards:list, k:int, maxTime:int) -> bool:

    painter = 1
    currBoards = 0

    for board in boards:
        currBoards+=board 
        if currBoards > maxTime:
            painter+=1
            currBoards = board 
    
    return painter <=k