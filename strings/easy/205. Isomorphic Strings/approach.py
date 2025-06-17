class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        if not self.checkIfSameCharsMapped(s,t) or not self.checkSameFrequence(s,t):
            return False
        
        return True
        
    def checkSameFrequence(self, s:str, t:str) -> bool:

        freq1, freq2 = dict(), dict()

        for ch in s:
            freq1[ch] = freq1.get(ch,0)+1

        for ch in t:
            freq2[ch] = freq2.get(ch,0)+1

        v1, v2 = freq1.values(), freq2.values()
        v1 = sorted(list(v1))
        v2 = sorted(list(v2))

        if len(v1)!=len(v2):
            return False
        
        for index, val in enumerate(v1):
            if val != v2[index]:
                return False

        return True


    def checkIfSameCharsMapped(self,s:str, t:str) -> bool:
        d = dict()
        for index, ch in enumerate(s):
            rep = t[index]

            if d.get(ch) is None:
                d[ch] = rep
            else:
                if d[ch]!=rep:
                    return False
        
        return True