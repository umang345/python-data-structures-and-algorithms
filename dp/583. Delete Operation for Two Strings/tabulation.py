class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        cache = [[0 for colIndex in range(m+1)] for rowIndex in range(n+1)]

        for index1 in range(1,n+1):
            for index2 in range(1,m+1):
                if word1[index1-1] == word2[index2-1]:
                    cache[index1][index2] = 1+cache[index1-1][index2-1]
                else:
                    cache[index1][index2] = max(
                        cache[index1-1][index2-1],
                        max(
                            cache[index1][index2-1],
                            cache[index1-1][index2]
                        )
                    )

        lcm = cache[n][m]
        return (n+m) - (2*lcm)