class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cache = [[-1 for col in range(n+1)] for row in range(n+1)]
        return self.helper(0,n, cuts, cache)

    def helper(self, start:int, end:int, cuts:list, cache:list) -> int:

        if start == end or start+1==end:
            return 0

        if cache[start][end]!=-1:
            return cache[start][end]

        currLen = end - start
        currentMin = None

        for index in cuts:
            if index > start and index < end:
                currCost = self.helper(start,index, cuts,cache) + self.helper(index,end, cuts,cache) + currLen
                if currentMin is None or currentMin > currCost:
                    currentMin = currCost
        
        if currentMin is None:
            cache[start][end] = 0
        else:
            cache[start][end] = currentMin

        return cache[start][end]