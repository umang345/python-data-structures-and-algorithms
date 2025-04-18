class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(len(s), len(p), s,p)

    def helper(self, index1, index2, s,p) -> bool:
        if index1==0 and index2==0:
            return True

        if index2==0:
            return False
        
        if index1==0:
            if p[index2-1] != "*":
                return False
            return self.helper(index1, index2-1, s,p)

        if p[index2-1]=="*":
            return self.helper(index1, index2-1,s,p) or self.helper(index1-1, index2,s,p) or self.helper(index1-1, index2-1, s,p)

        elif p[index2-1]=="?" or s[index1-1] == p[index2-1]:
            return self.helper(index1-1, index2-1,s,p)
        
        else:
            return False