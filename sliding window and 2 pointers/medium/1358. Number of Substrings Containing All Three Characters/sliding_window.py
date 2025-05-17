class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        start,end=0,0
        count=0
        hashMap = {
            'a':0,
            'b':0,
            'c':0
        }

        while end < len(s):
            
            hashMap[s[end]]+=1
            while hashMap['a']>0 and hashMap['b']>0 and hashMap['c']>0:
                count+=(len(s)-end)
                hashMap[s[start]]-=1
                start+=1
            
            end+=1
        
        return count