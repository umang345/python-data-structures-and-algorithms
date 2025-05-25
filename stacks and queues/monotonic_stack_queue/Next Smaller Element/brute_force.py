def nextSmallerElement(arr,n):
    
    result = [-1]*n

    for index in range(n):
        for nextIndex in range(index+1, n):
            if arr[nextIndex] < arr[index]:
                result[index] = arr[nextIndex]
                break
    
    return result
