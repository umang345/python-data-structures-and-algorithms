class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        cache = [0 for colIndex in range(n+1)]

        front = s
        back = "".join(list(reversed(s)))

        for row in range(1, n+1):
            tempCache = [0 for colIndex in range(n+1)]
            for col in range(1, n+1):
                if front[row-1] == back[col-1]:
                    tempCache[col] = 1+cache[col-1]
                else:
                    tempCache[col] = max(
                        cache[col-1],
                        max(
                            cache[col],
                            tempCache[col-1]
                        )
                    )
            for cacheIndex in range(n+1):
                cache[cacheIndex] = tempCache[cacheIndex]

        return cache[n]