class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []

        start = 0

        count = 0
        for index, ch in enumerate(s):
            if ch=="(":
                count+=1
            else:
                count-=1
            
            if count == 0:
                result.append(s[start+1: index])
                start = index+1
    
        return "".join(result)