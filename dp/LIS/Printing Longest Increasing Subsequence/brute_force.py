from typing import List
from functools import reduce


def printingLongestIncreasingSubsequence(arr: List[int], n: int) -> List[int]:
    
    return helper(0,-1,list(), arr)

def helper(index, pickedIndex, selected ,arr) -> list:
    if index == len(arr):
        return list(selected)
        
    notPicked = helper(index+1, pickedIndex, selected, arr)
    picked = []
    
    if pickedIndex == -1 or arr[index] > arr[pickedIndex]:
        selected.append(arr[index])
        picked = helper(index+1, index, selected, arr)
        selected.pop()

    if len(picked) > len(notPicked):
        return picked

    return notPicked