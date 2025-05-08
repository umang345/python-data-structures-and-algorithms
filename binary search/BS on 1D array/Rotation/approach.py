from math import *

def findKRotation(arr : list) -> int:
    
    minIndex,minElement = -1, inf

    start,end = 0, len(arr)-1

    while start<=end:
        mid = start + (end-start)//2
        if arr[start]<=arr[mid]:
            if minElement>arr[start]:
                minElement = arr[start]
                minIndex = start 
            start = mid+1
        else:
            if minElement>arr[mid]:
                minElement = arr[mid]
                minIndex = mid 
            end = mid-1
    
    return minIndex
