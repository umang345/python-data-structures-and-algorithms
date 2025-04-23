class Solution:
    def minCut(self, s: str) -> int:
        cache = [[-1 for end in range(len(s))] for start in range(len(s))]
        return self.helper(0, len(s)-1, s, cache)

    def helper(self, start, end, s, cache) -> int:
        if start == end or self.checkForPalindrome(s, start, end):
            return 0
        
        if cache[start][end]!=-1:
            return cache[start][end]

        minCuts = None
        for index in range(start+1, end+1):
            if self.checkForPalindrome(s, start, index-1):
                cuts = 1+self.helper(index, end, s, cache)
                if minCuts is None or minCuts > cuts:
                    minCuts = cuts
        if minCuts is None:
            minCuts = 0
        cache[start][end] = minCuts
        return cache[start][end]