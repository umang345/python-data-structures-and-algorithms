class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s), len(p)
        cache = [[None for col in range(m+1)] for row in range(n+1)]
        return self.helper(len(s), len(p), s,p, cache)

    def helper(self, index1, index2, s,p, cache) -> bool:
        if index1==0 and index2==0:
            return True

        if index2==0:
            return False
        
        if index1==0:
            if p[index2-1] != "*":
                return False
            return self.helper(index1, index2-1, s,p, cache)

        if not cache[index1][index2] is None:
            return cache[index1][index2]


        if p[index2-1]=="*":
            cache[index1][index2] = self.helper(index1, index2-1,s,p, cache) or self.helper(index1-1, index2,s,p, cache) or self.helper(index1-1, index2-1, s,p, cache)

        elif p[index2-1]=="?" or s[index1-1] == p[index2-1]:
            cache[index1][index2] = self.helper(index1-1, index2-1,s,p, cache)
        
        else:
            cache[index1][index2] = False

        return cache[index1][index2]