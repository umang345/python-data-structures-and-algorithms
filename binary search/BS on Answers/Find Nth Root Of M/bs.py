def NthRoot(n: int, m: int) -> int:
    if m==0:
        return 0
    low, high = 1, m

    while low<=high:
        mid = low + (high-low)//2
        currRootStatus = checkForRoot(n,mid,m)
        if currRootStatus == 0:
            return mid
        elif currRootStatus == 2:
            high = mid-1
        else:
            low = mid+1
    
    return -1
        

def checkForRoot(n:int, root:int,m:int) -> int:
    '''
    0 -> root^n == m
    1 -> root^n < m
    2 -> root^n >m
    '''

    num = 1
    for index in range(n):
        num*=root 
        if num > m:
            return 2

    if num==m:
        return 0
    
    return 1

'''
TC    log(m) * n
'''