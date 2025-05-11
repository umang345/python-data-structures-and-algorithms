from functools import *

def findLargestMinDistance(boards:list, k:int):
    
    maxElement = reduce(lambda acc,x : max(acc,x), boards,boards[0])
    totalSum = reduce(lambda acc,x : acc+x, boards,0)

    for maxTime in range(maxElement, totalSum+1):
        if helper(boards, k, maxTime):
            return maxTime
    
    return -1

def helper(boards:list, k:int, maxTime:int) -> bool:

    painter = 1
    currBoards = 0

    for board in boards:
        currBoards+=board 
        if currBoards > maxTime:
            painter+=1
            currBoards = board 
    
    return painter <=k