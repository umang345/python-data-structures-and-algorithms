class Solution:
    def minCut(self, s: str) -> int:
        cache = [[0 for end in range(len(s))] for start in range(len(s))]
        palin = [[False for end in range(len(s))] for start in range(len(s))]
        
        self.computePalindromes(s,palin)

        n = len(s)
        for start in range(n-1,-1,-1):
            for end in range(start,n):
                if start == end or self.checkForPalindrome(s, start, end):
                    cache[start][end] = 0
                    continue
                
                minCuts = None
                for index in range(start+1, end+1):
                    if self.checkForPalindrome(s, start, index-1):
                        cuts = 1+cache[index][end]
                        if minCuts is None or minCuts > cuts:
                            minCuts = cuts
                if minCuts is None:
                    minCuts = 0
                cache[start][end] = minCuts
        
        return cache[0][n-1]