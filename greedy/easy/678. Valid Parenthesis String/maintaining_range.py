class Solution:
    def checkValidString(self, s: str) -> bool:
        minLimit, maxLimit = 0,0

        for _, char in enumerate(s):
            if char == '(':
                minLimit+=1
                maxLimit+=1
            elif char == ')':
                minLimit = max(0, minLimit-1)
                maxLimit-=1
            else:
                minLimit = max(0, minLimit-1)
                maxLimit+=1
            
            if maxLimit<0:
                return False
        
        return minLimit==0