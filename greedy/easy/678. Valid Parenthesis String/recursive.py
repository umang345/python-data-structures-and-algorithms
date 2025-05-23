class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.helper(s, 0, 0)

    def helper(self, s:str,index:int, count:int):
        if index>=len(s):
            return count==0
        
        if s[index]=='(':
            return self.helper(s, index+1, count+1)
        elif s[index]==')':
            if count-1<0:
                return False
            return self.helper(s, index+1, count-1)
        else:
            leftBrace = self.helper(s, index+1, count+1)
            rightBrace = False if count-1<0 else self.helper(s, index+1, count-1)
            emptyStr = self.helper(s, index+1, count)

            return leftBrace or rightBrace or emptyStr
        
        