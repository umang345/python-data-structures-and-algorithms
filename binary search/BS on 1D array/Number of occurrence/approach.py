from typing import *

def count(arr: [int], n: int, x: int) -> int:
    
    firstOcc = first(arr,n,x)
    if firstOcc == -1:
        return 0
    
    lastOcc = last(arr,n,x)
    return lastOcc - firstOcc +1


def first(arr: [int], n:int, x:int) -> int:

    result,start,end = -1,0,n-1

    while start<=end:
        mid = start + (end-start)//2
        if arr[mid]==x:
            result = mid 

        if arr[mid] >= x:
            end = mid-1
        else:
            start = mid+1
    
    return result 

def last(arr:[int], n:int, x:int) -> int:

    result,start, end = -1,0,n-1

    while start<=end:
        mid = start + (end-start)//2
        if arr[mid]==x:
            result = mid 
        
        if arr[mid] <= x:
            start = mid+1
        else:
            end = mid-1

    return result
