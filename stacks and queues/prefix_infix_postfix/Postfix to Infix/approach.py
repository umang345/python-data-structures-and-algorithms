from collections import deque

def postToInfix(postfix: str) -> str:
    
    stack = deque()

    for char in postfix:
        if char.isalnum():
            stack.append(char)
        else:
            if len(stack) < 2:
                raise Exception("Invalid Postfix expression")
            
            exp1, exp2 = stack.pop(), stack.pop()
            opExp = "("+exp2+char+exp1+")"
            stack.append(opExp)

    return stack.pop() 
    