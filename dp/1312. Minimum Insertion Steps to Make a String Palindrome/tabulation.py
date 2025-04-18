class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        front = s
        back = "".join(list(reversed(s)))
        cache = [[0 for colInde in range(n+1)] for rowIndex in range(n+1)]
        
        for index1 in range(1, n+1):
            for index2 in range(1,n+1):
                if front[index1-1]==back[index2-1]:
                    cache[index1][index2] = 1+cache[index1-1][index2-1]
                else:
                    cache[index1][index2] = max(
                        cache[index1-1][index2-1],
                        max(
                            cache[index1][index2-1],
                            cache[index1-1][index2]
                        )
                    )

        return n - cache[n][n]