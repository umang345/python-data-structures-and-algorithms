from typing import List
from functools import reduce

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    total = reduce(lambda acc,x : acc+x, arr, 0)
    return helper(len(arr)-1, 0, total, arr)

def helper(index, sumSoFar, totalSum, arr):
    if index <0:
        div1 = sumSoFar 
        div2 = totalSum - sumSoFar 
        return abs(div1 - div2)

    return min(
        helper(index-1, sumSoFar+arr[index], totalSum, arr),
        helper(index-1, sumSoFar, totalSum, arr)
    )