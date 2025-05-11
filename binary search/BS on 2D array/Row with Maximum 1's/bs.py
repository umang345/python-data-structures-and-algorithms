from os import *
from sys import *
from collections import *
from math import *

def rowMaxOnes(mat, n, m):
    
    minColIndex = m 
    resultRowIndex = -1
    
    for rowIndex,row in enumerate(mat):
        indexOf1 = bsOn1DArray(row)
        if indexOf1!=-1:
            if minColIndex > indexOf1:
                minColIndex = indexOf1
                resultRowIndex = rowIndex 
    
    return resultRowIndex

def bsOn1DArray(nums:list) -> int:

    low, high = 0, len(nums)-1
    while low<=high:
        mid = low + (high-low)//2
        if nums[mid]==1:
            high = mid-1
        else:
            low = mid+1
    
    return low if low<len(nums) else -1