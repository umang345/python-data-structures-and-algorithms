class Solution:
    '''
    TC  O((n+n)*(n))
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxLen = 0
        start, end = 0,0
        hashMap = dict()

        while end<len(s):
            hashMap[s[end]] = hashMap.get(s[end],0) + 1

            while self.getRequiredConversions(hashMap, start, end) > k:
                hashMap[s[start]]-=1
                start+=1
            
            currLen = end-start+1
            maxLen = max(currLen, maxLen)
            end+=1
        
        return maxLen


    def getRequiredConversions(self, hashMap:dict, start:int, end:int) -> int:

        maxFreq = max(hashMap.values())
        return (end-start+1) - maxFreq 