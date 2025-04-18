class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        cache = [[0 for colIndex in range(n+1)] for colIndex in range(n+1)]

        front = s
        back = "".join(list(reversed(s)))

        for row in range(1, n+1):
            for col in range(1, n+1):
                if front[row-1] == back[col-1]:
                    cache[row][col] = 1+cache[row-1][col-1]
                else:
                    cache[row][col] = max(
                        cache[row-1][col-1],
                        max(
                            cache[row-1][col],
                            cache[row][col-1]
                        )
                    )

        return cache[n][n]