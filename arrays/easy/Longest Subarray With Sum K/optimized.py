def longestSubarrayWithSumK(a:list, k: int) -> int:
    start = 0
    end = -1
    currentSum = 0

    maxLen = 0

    while end<len(a)-1:
        end+=1
        currentSum+=a[end]

        if currentSum==k:
            currLen = end-start+1
            if maxLen<currLen:
                maxLen = currLen
        elif currentSum>k:
            while currentSum>k and start<=end:
                currentSum-=a[start]
                start+=1
            if currentSum==k:
                currLen = end-start+1
                if maxLen<currLen:
                    maxLen = currLen

                
    return maxLen