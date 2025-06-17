class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        f1, f2 = dict(), dict()

        for ch in s:
            f1[ch] = f1.get(ch,0)+1

        for ch in t:
            f2[ch] = f2.get(ch,0)+1

        for key, val in f1.items():
            if f2.get(key) is None or f2[key]!=val:
                return False

        for key, val in f2.items():
            if f1.get(key) is None or f1[key]!=val:
                return False
        
        return True