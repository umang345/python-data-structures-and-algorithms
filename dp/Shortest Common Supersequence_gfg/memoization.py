class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, s1, s2):
         n = len(s1)
         m = len(s2)
         cache = [[-1 for colIndex in range(m+1)] for rowIndex in range(n+1)]
         lcs = self.helper(n,m,s1,s2, cache)
         return ((n+m) - lcs)
         
    def helper(self, n,m,s1,s2, cache)->int:
        if n==0 or m==0:
            return 0
            
        if cache[n][m] != -1:
            return cache[n][m]
            
        if s1[n-1]==s2[m-1]:
            cache[n][m] = 1+self.helper(n-1, m-1, s1,s2,cache)
        else:
            cache[n][m] = max(
                    self.helper(n-1, m-1, s1,s2,cache),
                    max(
                        self.helper(n, m-1, s1,s2,cache),
                        self.helper(n-1, m, s1,s2,cache)
                        )
                )
        return cache[n][m]