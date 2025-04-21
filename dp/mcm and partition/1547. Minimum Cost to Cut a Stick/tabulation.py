class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cache = [[0 for col in range(n+1)] for row in range(n+1)]
        
        for start in range(n, -1,-1):
            for end in range(start, n+1):
                if end-start<=1:
                    continue

                currLen = end - start
                currentMin = None

                for index in cuts:
                    if index > start and index < end:
                        currCost = cache[start][index] + cache[index][end] + currLen
                        if currentMin is None or currentMin > currCost:
                            currentMin = currCost

                if not currentMin is None:
                    cache[start][end] = currentMin

        return cache[0][n]