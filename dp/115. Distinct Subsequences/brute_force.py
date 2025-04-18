class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        return self.helper(n,m,s,t)

    def helper(self, index1, index2, source, target) -> int:
        if index2 ==0 :
            return 1
        if index1 == 0:
            return 0

        if source[index1-1] == target[index2-1]:
            return self.helper(index1-1, index2-1, source, target) + self.helper(index1-1, index2, source, target)
        else:
            return self.helper(index1-1, index2, source,target)