class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        abcpabrtec
        '''
        maxLen = 0
        for startIndex in range(len(s)):
            hashSet = set()
            currLen = 0
            for index in range(startIndex, len(s)):
                if s[index] in hashSet:
                    break
                currLen+=1
                maxLen = max(currLen, maxLen)
                hashSet.add(s[index])
        
        return maxLen