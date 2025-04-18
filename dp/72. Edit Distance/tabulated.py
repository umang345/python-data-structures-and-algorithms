class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1), len(word2)
        cache = [[0 for colIndex in range(m+1)] for index in range(n+1)]
        
        for rowIndex in range(n+1):
            cache[rowIndex][0] = rowIndex
        
        for colIndex in range(m+1):
            cache[0][colIndex] = colIndex

        for rowIndex in range(1, n+1):
            for colIndex in range(1, m+1):
                if word1[rowIndex-1]==word2[colIndex-1]:
                    cache[rowIndex][colIndex] = cache[rowIndex-1][colIndex-1]
                else:
                    cache[rowIndex][colIndex] = 1+min(
                        cache[rowIndex-1][colIndex], min(
                            cache[rowIndex-1][colIndex-1],
                            cache[rowIndex][colIndex-1]
                        )
                    )

        return cache[n][m]