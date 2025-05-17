class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        abcabcbb
        '''
        hashSet = set()

        maxLen = 0
        start,end = 0,0
        while end < len(s):
            if s[end] in hashSet:
                while s[end] in hashSet and start<=end:
                    hashSet.remove(s[start])
                    start+=1
            
            currLen = end-start+1   
            maxLen = max(currLen, maxLen)
            hashSet.add(s[end])
            end+=1
        
        return maxLen
    
'''
TC  ->  O(n)+O(n)
'''