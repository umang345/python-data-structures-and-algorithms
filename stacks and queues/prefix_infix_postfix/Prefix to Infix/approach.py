from collections import deque

def prefixToInfixConversion(s: str) -> str:
    stack = deque()

    for index in range(len(s)-1, -1,-1):
        char = s[index]
        if char.isalnum():
            stack.append(char)
        else:
            if len(stack)<2:
                raise Exception("Invalid prefix expression")
            
            stNum1, stNum2 = stack.pop(), stack.pop()
            opStr = "("+stNum1+char+stNum2+")"
            stack.append(opStr)
    
    return stack.pop()