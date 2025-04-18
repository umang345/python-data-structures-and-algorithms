class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        cache =[[-1 for colIndex in range(m+1)] for rowIndex in range(n+1)]
        return self.helper(n,m,s,t, cache)

    def helper(self, index1, index2, source, target, cache:list) -> int:
        if index2 ==0 :
            return 1
        if index1 == 0:
            return 0

        if cache[index1][index2] != -1:
            return cache[index1][index2]

        if source[index1-1] == target[index2-1]:
            cache[index1][index2] = self.helper(index1-1, index2-1, source, target,cache) + self.helper(index1-1, index2, source, target,cache)
        else:
            cache[index1][index2] = self.helper(index1-1, index2, source,target,cache)

        return cache[index1][index2]