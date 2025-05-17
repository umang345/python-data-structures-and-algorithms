class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        
        for startIndex in range(len(s)):
            hashSet = set()
            for index in range(startIndex,len(s)):
                hashSet.add(s[index])
                if len(hashSet) == 3:
                    count+=(len(s)-index)
                    break
        
        return count