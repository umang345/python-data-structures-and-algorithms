def kDistinctChars(k, string):
    start=0
    maxLen = 0
    n = len(string)
    hashMap = dict()

    for end in range(n):
        hashMap[string[end]] = hashMap.get(string[end],0)+1
        
        if len(hashMap.keys()) > k :
            hashMap[string[start]]-=1
            if hashMap[string[start]]==0:
                del hashMap[string[start]]
            start+=1
        
        if len(hashMap.keys()) <=k:
            currLen = end-start+1
            maxLen = max(maxLen, currLen)
    
    return maxLen