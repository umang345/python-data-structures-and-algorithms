from math import *

def aggressiveCows(stalls, k):
    stalls.sort()

    maxDistance = stalls[-1]

    result = -inf
    low,high = 1,maxDistance

    while low<=high:
        dis = low + (high-low)//2
        
        if helper(stalls,k,dis):
            result = max(result, dis)
            low = dis+1
        else:
            high = dis-1
    
    return result


def helper(stalls,k,dis) -> bool:
    last = stalls[0]
    cows = 1

    for index in range(1, len(stalls)):
        if stalls[index]-last >= dis:
            last = stalls[index]
            cows+=1
    
    return cows >= k