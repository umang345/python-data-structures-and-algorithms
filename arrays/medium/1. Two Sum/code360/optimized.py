def twoSum(arr, target, n):
    
    result = []
    arr.sort()
    start, end = 0, len(arr)-1

    while start<end:
        sumToCheck = arr[start] + arr[end]
        if sumToCheck == target:
            result.append([arr[start], arr[end]])
            start+=1
            end-=1
        elif sumToCheck < target:
            start+=1
        else:
            end-=1
    
    if len(result)==0:
        result.append([-1,-1])
    
    return result

'''
TC  ->   O(nlogn) + O(n) -> O(nlogn)
SC  ->   O(1)
'''