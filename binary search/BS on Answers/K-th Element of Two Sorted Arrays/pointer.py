def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
    
    index,p1,p2 = 0,0,0
    currElement = -1

    while index < k:
        if arr1[p1] <= arr2[p2]:
            currElement = arr1[p1]
            p1+=1
        else:
            currElement = arr2[p2]
            p2+=1
        index+=1
    
    return currElement
