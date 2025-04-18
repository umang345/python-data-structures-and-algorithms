class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        cache =[[0 for colIndex in range(m+1)] for rowIndex in range(n+1)]
        
        for rowIndex in range(n+1):
            cache[rowIndex][0] = 1
        
        for rowIndex in range(1, n+1):
            for colIndex in range(1, m+1):
                if s[rowIndex-1] == t[colIndex-1]:
                    cache[rowIndex][colIndex] = cache[rowIndex-1][colIndex-1] + cache[rowIndex-1][colIndex]
                else:
                    cache[rowIndex][colIndex] = cache[rowIndex-1][colIndex]
        
        return cache[n][m]