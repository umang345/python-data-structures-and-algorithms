class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, s1, s2):
         n = len(s1)
         m = len(s2)
         cache = [[0 for colIndex in range(m+1)] for rowIndex in range(n+1)]
         
         for row in range(1, n+1):
             for col in range(1, m+1):
                 
                if s1[row-1]==s2[col-1]:
                    cache[row][col] = 1+cache[row-1][col-1]
                else:
                    cache[row][col] = max(
                            cache[row-1][col-1], 
                            max(
                                    cache[row-1][col],
                                    cache[row][col-1]
                                )
                        )
                        
                        
         
         
         lcs = cache[n][m]
         return ((n+m) - lcs)