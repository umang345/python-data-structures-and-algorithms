from typing import List

def longestBitonicSubsequence(arr: List[int], n: int) -> int:
    
    lisIncreasing = [1 for index in range(n)]
    lisDecreasing = [1 for index in range(n)]

    for index in range(n):
        for compare in range(index):
            if arr[index] > arr[compare] and lisIncreasing[index] <= lisIncreasing[compare]:
                lisIncreasing[index] = 1+lisIncreasing[compare]
    
    for index in range(n-1, -1, -1):
        for compare in range(n-1,index,-1):
            if arr[index] > arr[compare] and lisDecreasing[index] <= lisDecreasing[compare]:
                lisDecreasing[index] = 1+lisDecreasing[compare]

    bitonic =0
    for index in range(n):
        bitonic = max(bitonic, lisIncreasing[index]+lisDecreasing[index]-1)
    
    return bitonic