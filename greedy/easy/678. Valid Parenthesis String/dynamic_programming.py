class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.helper(s, 0, 0, dict())

    def helper(self, s:str,index:int, count:int, dp:dict):
        if index>=len(s):
            return count==0
        
        key = f"{index}_{count}"
        if not dp.get(key) is None:
            return dp[key]

        if s[index]=='(':
            dp[key] = self.helper(s, index+1, count+1,dp)
        elif s[index]==')':
            if count-1<0:
                dp[key] = False
            else:
                dp[key] = self.helper(s, index+1, count-1,dp)
        else:
            leftBrace = self.helper(s, index+1, count+1,dp)
            rightBrace = False if count-1<0 else self.helper(s, index+1, count-1,dp)
            emptyStr = self.helper(s, index+1, count,dp)

            dp[key] = leftBrace or rightBrace or emptyStr
        
        return dp[key]