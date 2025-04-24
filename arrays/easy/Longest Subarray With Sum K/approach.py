def longestSubarrayWithSumK(a: [int], k: int) -> int:
    maxLen = 0
    for startIndex in range(len(a)):
        currSum = 0
        currIndex = startIndex 
        while currIndex < len(a):
            if currSum+a[currIndex] > k:
                break 
            currSum += a[currIndex]
            currIndex+=1
        
        if currSum==k:
            currLen = currIndex - startIndex
            if maxLen<currLen:
                maxLen = currLen 
    
    return maxLen
        
