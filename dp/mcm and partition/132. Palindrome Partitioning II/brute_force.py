class Solution:
    def minCut(self, s: str) -> int:
        return self.helper(0, len(s)-1, s)

    def helper(self, start, end, s) -> int:
        print(f"Helper() -> start={start} , end={end}")
        if start == end or self.checkForPalindrome(s, start, end):
            return 0

        minCuts = None
        for index in range(start+1, end+1):
            if self.checkForPalindrome(s, start, index-1):
                cuts = 1+self.helper(index, end, s)
                if minCuts is None or minCuts > cuts:
                    minCuts = cuts
        if minCuts is None:
            minCuts = 0
        return minCuts


    def checkForPalindrome(self, s:str, start:int, end:int) -> bool:
        while start < end:
            if s[start]!=s[end]:
                return False 
            start+=1
            end-=1
        
        return True
    
sol = Solution()
print(sol.minCut("ab"))