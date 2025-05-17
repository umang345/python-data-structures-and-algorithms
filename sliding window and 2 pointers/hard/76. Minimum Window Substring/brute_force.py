class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        
        targetMap = dict()
        for char in t:
            targetMap[char] = targetMap.get(char,0)+1
        
        minString = None

        for startIndex in range(len(s)):
            hashMap = dict()
            for index in range(startIndex, len(s)):
                hashMap[s[index]] = hashMap.get(s[index],0)+1
                if self.compareMaps(hashMap, targetMap):
                    if minString is None or len(minString) > (index-startIndex+1):
                        minString = s[startIndex:index+1]
        
        return minString
    
    def compareMaps(self, map1:dict, target:dict) -> bool:
        for key, val in target.items():
            if val != map1.get(key,0):
                return False
        
        return True
        