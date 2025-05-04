def getInversions(arr, n):
    count = 0
    for curr in range(n):
        for nextIndex in range(curr+1, n):
            if arr[curr]>arr[nextIndex]:
                count+=1
    return count