def getFloorAndCeil(a, n, x):
    return [floor(a,n,x), ceil(a,n,x)]

def floor(a,n,x):
    result = -1
    start,end = 0,n-1

    while start<=end:
        mid = start + (end-start)//2
        if a[mid]<=x:
            result = mid 
            start = mid+1
        else:
            end = mid-1
    
    if result==-1:
        return -1
    return a[result]

def ceil(a,n,x):

    result = -1
    start,end = 0,n-1

    while start<=end:
        mid = start + (end-start)//2
        if a[mid]>=x:
            result = mid
            end = mid-1
        else:
            start = mid+1

    if result == -1:
        return -1
    return a[result]