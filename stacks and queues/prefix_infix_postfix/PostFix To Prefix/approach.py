from collections import deque

def postfixToPrefix(s: str) -> str:
    
    stack = deque()
    for char in s:
        if char.isalnum():
            stack.append(char)
        else:
            exp1, exp2 = stack.pop(), stack.pop()
            opStr = char+exp2+exp1
            stack.append(opStr)
    
    return stack.pop()