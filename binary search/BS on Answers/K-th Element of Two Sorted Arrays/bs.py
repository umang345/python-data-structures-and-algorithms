from math import *

def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
    if n>m:
        return kthElement(arr2,m,arr1,n,k)
    

    high = min(k,n)
    low = max(0, k-m)
    while low<=high:
        mid = low+(high-low)//2
        left1 = arr1[mid-1] if mid-1>=0 else -inf
        right1 = arr1[mid] if mid<n else inf 
        left2 = arr2[k - mid - 1] if k-mid-1>=0 else -inf
        right2 = arr2[k-mid] if k-mid < m else inf 

        if left1<=right2 and left2<=right1:
            return max(left1, left2)

        if left1>right2:
            high = mid-1
        else:
            low = mid+1

    return -1 
        
