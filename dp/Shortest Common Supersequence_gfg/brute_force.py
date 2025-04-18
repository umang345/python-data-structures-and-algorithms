class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, s1, s2):
         n = len(s1)
         m = len(s2)
         lcs = self.helper(n,m,s1,s2)
         return ((n+m) - lcs)
         
    def helper(self, n,m,s1,s2)->int:
        if n==0 or m==0:
            return 0
            
        if s1[n-1]==s2[m-1]:
            return 1+self.helper(n-1, m-1, s1,s2)
        else:
            return max(
                    self.helper(n-1, m-1, s1,s2),
                    max(
                        self.helper(n, m-1, s1,s2),
                        self.helper(n-1, m, s1,s2)
                        )
                )