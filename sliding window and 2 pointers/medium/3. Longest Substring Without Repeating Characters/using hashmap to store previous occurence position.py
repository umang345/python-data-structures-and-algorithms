class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashMap = dict()
        start, end = 0,0
        maxLen = 0

        while end < len(s):
            if s[end] in hashMap.keys() and hashMap[s[end]] >= start:
                start = hashMap[s[end]]+1
            
            currLen = end - start + 1
            maxLen = max(maxLen, currLen)
            hashMap[s[end]] = end
            end+=1
        
        return maxLen