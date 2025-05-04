def getInversions(arr, n):
    
    '''  "13"
    [4,6,1,5,9,3,8,7,2]
    
        "3" "4" "4" "1" "1"                              "1"
    [1,4,5,6,9]                    [2,3,7,8]

      "2" "1"     "0"                            "1"
    [1,4,6]      [5,9]           [3,8]         [7,2]

        
    [4,6]   [1]   [5] [9]     [3]    [8]    [7]       [2]
    

    [4]   [6]
    
    [] []  []   []
    
    '''
    return helper(arr, 0, len(arr)-1, n)

def helper(arr,start,end,n)->int:
    if start>=end:
        return 0

    mid = start + (end-start)//2

    leftSubArrayCount = helper(arr,start,mid,n)
    rightSubArratCount = helper(arr,mid+1, end, n)

    currCount = 0
    index1, index2 = start,mid+1
    while index1<=mid and index2<=end:
        if arr[index1]<arr[index2]:
            index1+=1
        else:
            currLen = mid-index1+1
            currCount+=currLen 
            index2+=1
    
    temp = [-1]*(end-start+1)
    tempIndex = 0
    index1, index2 = start, mid+1

    while index1<=mid and index2<=end:
        if arr[index1]<arr[index2]:
            temp[tempIndex] = arr[index1]
            index1+=1
        else:
            temp[tempIndex] = arr[index2]
            index2+=1
        tempIndex+=1
    
    while index1<=mid:
        temp[tempIndex] = arr[index1]
        index1+=1
        tempIndex+=1
    while index2<=end:
        temp[tempIndex] = arr[index2]
        index2+=1
        tempIndex+=1
    
    for index in range(start,end+1):
        arr[index] = temp[index-start]

    return currCount+leftSubArrayCount+rightSubArratCount


'''
TC -> O(nlogn)
SC -> O(n)
'''