class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0

        for startIndex in range(len(s)):
            currLen = 0
            hashMap = dict()

            for index in range(startIndex, len(s)):
                hashMap[s[index]] = hashMap.get(s[index],0)+1
                if self.getRequiredConversions(hashMap,startIndex, index) > k:
                    break
                currLen+=1
                maxLen = max(maxLen, currLen)
        
        return maxLen


    def getRequiredConversions(self, hashMap:dict, start:int, end:int) -> int:

        maxFreq = max(hashMap.values())
        return (end-start+1) - maxFreq 