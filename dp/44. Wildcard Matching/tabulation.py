class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s), len(p)
        cache = [[False for col in range(m+1)] for row in range(n+1)]
        cache[0][0] = True
        
        for rowIndex in range(n+1):
            for colIndex in range(1,m+1):
                if rowIndex == 0:
                    if p[colIndex-1]=="*":
                        cache[rowIndex][colIndex] = cache[rowIndex][colIndex-1]
                else:
                    if p[colIndex-1]=="*":
                        cache[rowIndex][colIndex] = cache[rowIndex-1][colIndex] or cache[rowIndex][colIndex-1] or cache[rowIndex-1][colIndex-1]
                    elif p[colIndex-1]=="?" or s[rowIndex-1] == p[colIndex-1]:
                        cache[rowIndex][colIndex] = cache[rowIndex-1][colIndex-1]
                    else:
                        cache[rowIndex][colIndex]

        return cache[n][m]