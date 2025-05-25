from collections import deque 

'''
1) Reverse the infix expression ->  flip ( and )
2) Convert to postfix
3) reverse the postfix
'''

def infixToPrefix(infix:str):

    revInfix = []
    for index in range(len(infix)-1,  -1,-1):
        if infix[index] == "(":
            revInfix.append(")")
        elif infix[index] == ")":
            revInfix.append("(")
        else:
            revInfix.append(infix[index])
    
    stack = deque()
    result = []

    for char in revInfix:
        if char.isalnum():
            result.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while len(stack)>0 and stack[-1]!="(":
                result.append(stack.pop())
            stack.pop()
        else:
            while len(stack)>0 and priority(char) <= priority(stack[-1]):
                result.append(stack.pop())
            
            stack.append(char)
    
    while len(stack)>0:
        result.append(stack.pop())
    
    return "".join(result.reverse())

            

def priority(char:str) -> int:
    if char == "^":
        return 3
    if char == "/" or char=="*":
        return 2 
    if char == "+" or char == "-":
        return 1
    return 0