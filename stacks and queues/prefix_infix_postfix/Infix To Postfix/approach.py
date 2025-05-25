from collections import deque

def infixToPostfix(exp: str) -> str:
    stack = deque()
    result = []
    for char in exp:
        if char.isalnum():
            result.append(char)
        elif char == '(':
            stack.appendleft(char)
        elif char == ')':
            while len(stack)>0 and stack[0] !="(":
                result.append(stack.popleft())
            
            if len(stack)==0:
                raise Exception("Invalid Infix expression")
            
            stack.popleft()

        else:
            while len(stack)>0 and priority(stack[0])>=priority(char):
                result.append(stack.popleft())
            
            stack.appendleft(char)
    
    while len(stack)>0:
        result.append(stack.popleft())
    
    return "".join(result)


def priority(char:str) -> int:
    if char == '^':
        return 3
    if char == '*' or char == '/':
        return 2
    if char == '+' or char == '-':
        return 1
    return 0