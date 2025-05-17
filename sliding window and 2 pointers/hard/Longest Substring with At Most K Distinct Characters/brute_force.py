def kDistinctChars(k, string):
    maxLen = 0
    n = len(string)
    for startIndex in range(n):
        hashSet = set()
        currLen = 0
        for index in range(startIndex, n):
            hashSet.add(string[index])
            currLen+=1
            if len(hashSet)>k:
                break
            
            maxLen = max(maxLen, currLen)
    return maxLen


