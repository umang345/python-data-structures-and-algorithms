def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
    
    merged = [0]*(n+m)
    index, p1, p2 = 0,0,0

    while p1<n and p2<m:
        if arr1[p1] <= arr2[p2]:
            merged[index] = arr1[p1]
            p1+=1
        else:
            merged[index] = arr2[p2]
            p2+=1
        index+=1
    
    while p1<n:
        merged[index] = arr1[p1]
        index+=1
        p1+=1
    
    while p2<m:
        merged[index] = arr2[p2]
        index+=1
        p2+=1
    
    return merged[k-1]
