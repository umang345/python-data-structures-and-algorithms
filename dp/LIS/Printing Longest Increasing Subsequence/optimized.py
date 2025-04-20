from typing import List

def printingLongestIncreasingSubsequence(arr: List[int], n: int) -> List[int]:
    
    dp = [1 for index in range(len(arr))]
    cache = [index for index in range(len(arr))]

    for index in range(len(arr)):
        for compare in range(index):
            if arr[index]>arr[compare] and dp[index] <= dp[compare]:
                dp[index] = 1 + dp[compare]
                cache[index] = compare 

    lis_len = 0
    lis = []

    for index in range(len(dp)):
        if dp[index] > lis_len:
            lis_len = dp[index]
            currSeq = getSequence(index,arr,cache)
            lis = currSeq

    return lis

def getSequence(index,arr,cache):
    seq = [arr[index]]
    while cache[index]!=index:
        seq.append(arr[cache[index]])
        index = cache[index]
    
    return list(reversed(seq))