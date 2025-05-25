from typing import List
from collections import deque

def preToPost(s: str) -> str:
    
    stack = deque()
    
    for index in range(len(s)-1,-1,-1):
        char = s[index]
        if char.isalnum():
            stack.append(char)
        else:
            if len(stack)<2:
                raise Exception("Invalid prefix expression")
            
            num1, num2 = stack.pop(), stack.pop()
            opStr = num1+num2+char
            stack.append(opStr)
    
    return stack.pop()

    