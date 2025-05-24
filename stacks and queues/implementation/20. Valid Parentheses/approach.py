from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        startingBraces = set(["(", "{", "["])
        corresOpeningBraces = dict()
        corresOpeningBraces[")"] = "("
        corresOpeningBraces["}"] = "{" 
        corresOpeningBraces["]"] = "["

        stack = deque()

        for brace in s:
            if brace in startingBraces:
                stack.append(brace)
            else:
                if len(stack)==0 or stack[-1]!=corresOpeningBraces[brace]:
                    return False
                stack.pop()
        
        return len(stack)==0
                