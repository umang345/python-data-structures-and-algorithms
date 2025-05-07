def lowerBound(arr: [int], n: int, x: int) -> int:
    if x>arr[n-1]:
        return n
    
    result = -1
    start, end = 0,n-1

    while start<=end:
        mid = start + (end-start)//2
        if arr[mid]>=x:
            result = mid 
            end = mid-1
        else:
            start = mid+1
    
    return result
