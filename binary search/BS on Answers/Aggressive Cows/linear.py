from math import *

def aggressiveCows(stalls, k):
    stalls.sort()

    maxDistance = stalls[-1]

    result = -inf
    for dis in range(1, maxDistance+1):

        isPos = helper(stalls,k,dis)
        if isPos:
            result = max(result,dis) 
    
    return result

def helper(stalls,k,dis):
    last = stalls[0]
    cows = 1

    for index in range(1, len(stalls)):
        if stalls[index]-last >= dis:
            last = stalls[index]
            cows+=1
    
    return cows >= k
    