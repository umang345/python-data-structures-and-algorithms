from math import *

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        
        targetMap = dict()
        for char in t:
            targetMap[char] = targetMap.get(char,0)+1
        
        minString = ""
        minLength = inf

        start = 0
        hashMap = dict()

        for end in range(len(s)):
            hashMap[s[end]] = hashMap.get(s[end],0)+1
            while self.compareMaps(hashMap, targetMap):
                currLen = end-start+1
                if currLen < minLength:
                    minString = s[start:end+1]
                    minLength = currLen
                hashMap[s[start]]-=1
                start+=1
            
        return minString
        
    
    def compareMaps(self, map1:dict, target:dict) -> bool:
        for key, val in target.items():
            if val > map1.get(key,0):
                return False
        
        return True